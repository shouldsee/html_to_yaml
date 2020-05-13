#!/usr/bin/env python3.7

s = '''
- caption:  fieldset msie5
  tinycap:  fieldset
  domain:   html
  desc:     fieldset and legend tag
  wwbody: |
    <fieldset>
    <legend>legend</legend>

    </fieldset>
- f:
   - a:
   - d: x
'''


import yaml


def str_dict_to_yaml(x):
  return ordered_dump(x, sort_keys=False, allow_unicode=True,)
  # return yaml.safe_dump(x, sort_keys=False, allow_unicode=True, )

def str_html_to_yaml(buf):
  x  = str_html_to_dict(buf)
  out= str_dict_to_yaml(x)
  return out 


def node_to_dict(x):
  o = collections.OrderedDict()
  # o['_#s'] = OrderedDict()
  o['_#t'] = x.tag
  for k,v in x.items(): o['_@%s'%k] = v; 
  o['_#c'] = []
  if x.text: o['_#c'].append({"_#r":x.text})
  
  res = x.getchildren()
  # if not len(res):
  #   return x
  for xx in res:
    o['_#c'].append(node_to_dict(xx))
    if xx.tail: o['_#c'].append({"_#r":xx.tail})
  # import pdb; pdb.set_trace()
  return o

def str_html_to_dict(buf):
  # x = ET.fromstring(buf, remove_comments=True)
  x = ET.parse(io.BytesIO(buf.encode()), parser =ET.XMLParser(remove_comments=True, remove_blank_text=True))
  x = x.getroot()
  # remove_comments=True)
  y = node_to_dict(x)
  return y

def dict_to_node(o, xpo, xlo):
  '''
  <o> current dict
  <xlo> node casted from the last dict
  <xpo> node casted from the parent dict

  '''
  if '_#t' not in o:
    assert '_#r' in o, o.keys()
    if xlo is None:
      ## this is the first child
      ## set text of parent node <xpo>
      xpo.text = o['_#r']
      return o
    elif isinstance(xlo, dict):
      raise Exception(f'Consecutive raw fields in list: [{xlo!r},{o!r}')
    else:  
      ## this is not the first child
      ## set tail of last node
      xlo.tail = o['_#r']
      return o
  else:
    assert '_#t' in o,o.keys()
    if '_#cr' in o:
      assert '_#c' not in o,o.keys()
      xpo = ET.Element(o.pop('_#t'))
      xpo.text = o.pop('_#cr')
    else:
      assert '_#c' in o,o.keys()
      xpo = ET.Element(o.pop('_#t'))
      xlo = None
      for oo in o.pop('_#c'):
        xlo = dict_to_node(oo, xpo, xlo)
        if not isinstance(xlo,dict):
          xpo.append(xlo)

      ## anything left should be an attribute field
    for k,v in o.items():
      assert k[:2] == '_@',o.keys()
      xpo.set(k[2:], v)

    # if len(o)>=2:
    #   pprint(['_#o',o])
      # import pdb; pdb.set_trace()
    return xpo


  pass

# import xml.etree.ElementTree as ET
import lxml.etree as ET
import collections
import io
def str_yaml_to_html(yy):
  yd = ordered_load(yy)
  xx = dict_to_node(yd, None, None)
  # xx = ET.tostring(xx,encoding='utf-8',short_empty_elements=False).decode()
  xx = ET.tostring(xx,encoding='utf-8').decode()
  return xx

  # buf = io.BytesIO()
  # xx = xx.getroottree().write_c14n( buf)
  #  # xml_declaration=True)
  # # , pretty_print=True)
  # buf.seek(0);
  # return buf.read().decode()


from pprint import pprint
import xmltodict
from collections import OrderedDict


'''
Source: https://stackoverflow.com/a/21912744/8083313
'''
def ordered_load(stream, Loader=yaml.Loader, object_pairs_hook=OrderedDict):
    class OrderedLoader(Loader):
        pass
    def construct_mapping(loader, node):
        loader.flatten_mapping(node)
        return object_pairs_hook(loader.construct_pairs(node))
    OrderedLoader.add_constructor(
        yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
        construct_mapping)
    return yaml.load(stream, OrderedLoader)

def ordered_dump(data, stream=None, Dumper=yaml.Dumper, **kwds):
    # pprint(data)cyfunction Comment at 0x7fd0ea257890

    class OrderedDumper(Dumper):
        pass
    def _dict_representer(dumper, data):
        return dumper.represent_mapping(
            yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
            data.items())
    OrderedDumper.add_representer(OrderedDict, _dict_representer)
    # OrderedDumper.add_representer(OrderedDict, _dict_representer)
    return yaml.dump(data, stream, OrderedDumper, **kwds)

def main():
  import argparse
  import sys,os
  parser = argparse.ArgumentParser()
  parser.add_argument('-f', '--from')
  parser.add_argument('src')
  parser.add_argument('-o', '--output')
  args = parser.parse_args()
  if args.output:
    output = open(args.output,'w')
  else:
    output = sys.stdout
  args.format = getattr(args,'from')
  with open(args.src,'rb') as f:
    inputBuffer = f.read().decode()
  if args.format == 'html':
    outputBuffer = str_html_to_yaml(inputBuffer)
  elif args.format=='yaml':
    outputBuffer = str_yaml_to_html(inputBuffer)
  else:
    assert 0,sys.argv
  output.write(outputBuffer)
  output.close()
  sys.exit(0)
  # test_main()

if __name__=='__main__':
  main()