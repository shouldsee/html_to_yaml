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

# import xml.etree.ElementTree as ET
import lxml.etree as ET
ETParser = ET.XMLParser(remove_comments=True, remove_blank_text=True, resolve_entities=False)
# ETParser = ET.XMLParser(remove_comments=True, remove_blank_text=True, resolve_entities=True)
# False)
# import lxml.html as ET
# ETParser = ET.HTMLParser(remove_comments=True, remove_blank_text=True)
# (self, encoding=None, remove_blank_text=False, remove_comments=False, remove_pis=False, strip_cdata=True, no_network=True, target=None, schema: XMLSchema=None, recover=True, compact=True, collect_ids=True, huge_tree=False)
# , resolve_entities=False)
import collections
import io

def str_dict_to_yaml(x):
  return ordered_dump(x, sort_keys=False, allow_unicode=True,)
  # return yaml.safe_dump(x, sort_keys=False, allow_unicode=True, )

def str_html_to_yaml(buf):
  x  = str_html_to_dict(buf)
  out= str_dict_to_yaml(x)
  return out 


def str_html_to_dict(buf,parser = ETParser):
  # x = ET.fromstring(buf, remove_comments=True)
  x = ET.parse(io.BytesIO(buf.encode()), parser = parser)
  # import pdb; pdb.set_trace()
  # x = x.getroot()
  # remove_comments=True)
  y = node_to_dict(x)
  return y


def node_to_dict(x):
  o   = collections.OrderedDict()
  # import pdb; pdb.set_trace()
  # o['_#s'] = OrderedDict()
  # tag = x.tag
  # print('[prefix]',x.sourceline)
  if 0:
    pass
  elif type(x) is ET._ElementTree:
    # ET.DocInfo:
    # import pdb; pdb.set_trace()
    # ET.DocInfo
    # xx = x.docinfo
    o['_']= 'D'   
    # o['root_name'] = x.docinfo.root_name
    # if x.docinfo.root_name == 'html':
    a = (x.docinfo.root_name,
      x.docinfo.public_id,
      x.docinfo.system_url,
      x.docinfo.doctype,)
    # import pdb; pdb.set_trace()
    # o.__setitem__('root_name', x.docinfo.root_name) 
    if x.docinfo.doctype:
      o['doctype'] = OrderedDict()
      o['doctype']['public_id']  = x.docinfo.public_id
      o['doctype']['system_url'] = x.docinfo.system_url
    oo = node_to_dict(x.getroot())
    o['_#c'] = [oo]
    assert x.docinfo.root_name == list(oo)[0],( x.docinfo.root_name,list(oo)[0])
    # .keys()[0]
    return o
  elif type(x) is ET._Element:
    o[x.tag] = 'T'
    for k,v in x.items(): o['%s'%k] = v; 
    o['_#c'] = []  
    if x.text: o['_#c'].append(x.text)
    # {"_#r":x.text})  
    res = x.getchildren()
    for xx in res:
      o['_#c'].append(node_to_dict(xx))
      if xx.tail: o['_#c'].append(xx.tail)
    # import pdb; pdb.set_trace()
    return o

  elif type(x) is ET._Entity:
    print('[E]',x)
    # import pdb; pdb.set_trace()
    o[x.name] ='E'
    text = f'&{x.name};'
    assert text == x.text,(text,x.text)
    o['_#c'] = []
    return o

  else:
    assert 0,(type(x),x, getattr(x,'tag',None))



def dict_to_node(o, xpo, xlo, buf):
  '''
  <o> current dict
  <xlo> node casted from the last dict
  <xpo> node casted from the parent dict

  '''
  if isinstance(o,str):
    if xlo is None:
      ## this is the first child
      ## set text of parent node <xpo>
      xpo.text = o
      return o
    elif isinstance(xlo, str):
      raise Exception(f'Consecutive raw fields in list: [{xlo!r},{o!r}')
    else:  
      ## this is not the first child
      ## set tail of last node
      xlo.tail = o
      return o
  elif isinstance(o,list):
    assert 0,('Undefined occurence of list %s'%(repr(o)[:200]))
  elif isinstance(o,dict):
    o = OrderedDict(o)
    oks = list(o)
    k = oks[0]
    v = o.pop(oks[0])
    if v is 'T':
      xpo = ET.Element(oks[0])

      for i,(k,v) in enumerate(o.items()):
        if k[:3] == '_#c':
          assert i+1 == len(o), (i, k, o.keys())
          break
        else:
          xpo.set(k, v)

      if oks[-1] == '_#cr':
        ### use _#cr to map to a _#c: [{_#r: innerHtml }] <--> _#cr: innterHtml
        xpo.text = o['_#cr']
      else:
        assert oks[-1] =='_#c'
        xlo = None
        for oo in o['_#c']:
          xlo = dict_to_node(oo, xpo, xlo, buf)
          if not isinstance(xlo,str):
            xpo.append(xlo)
      return xpo
    elif v is 'E':
      'this is an entity like &nbsp;. lets append to the text of parent node'
      # print('[dbg]',v.tag,v.text,v.prefix)
      # import pdb; pdb.set_trace()
      xpo = ET.Entity(k)
      # assert len(oks)==1
      return xpo
    elif v is 'D':
      assert k is '_',('Key must be _ when specifying D _: D ',k,v)
      # xpo = init_et_tree(o)
      oo = o['_#c'][0]
      root_name = list( oo )[0]
      xpo = ET.ElementTree( dict_to_node(oo, xpo, None, buf) )

      if 'doctype' in o:
        v = o['doctype']
        if isinstance(v,dict):
          xpo.docinfo.system_url = v['system_url']
          xpo.docinfo.public_id  = v['public_id']
        else:
          buf.write(f'<!DOCTYPE {root_name}>\n'.encode())
      return xpo


    else:
      assert 0,('Invalid node identifier', oks[0], v)

      ## anything left should be an attribute field
    # assert not len(o),('Not all keys processed. Only allowing _#t, _#c, _#cr',o.keys())

    # if len(o)>=2:
    #   pprint(['_#o',o])
      # import pdb; pdb.set_trace()
    # return xpo


  pass


def str_yaml_to_html(yy):
  yd  = ordered_load(yy)
  buf = io.BytesIO()
  xx  = dict_to_node(yd, None, None, buf)
  buf.write(ET.tostring(xx,encoding='utf-8'))
  buf.seek(0)
  return buf.read().decode()
  # import pdb; pdb.set_trace()

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
  parser.add_argument('--pdb',action='store_true',default=0)
  parser.add_argument('-f', '--from')
  parser.add_argument('src')
  parser.add_argument('-o', '--output')
  args = parser.parse_args()

  try:
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
    # sys.exit(0)
  except Exception as e:
    if args.pdb: 
      import traceback; traceback.print_exc()
      import pdb; pdb.post_mortem()
      sys.exit(1);
    else:
      raise


  # test_main()


# s = '''
# - _#t: html
#   _@lang: en
# - - - _#t: head
#     - - - _#t: meta
#           _@charset: utf-8
#         - []
#       - - _#t: title
#         - - _#r
#     - _#t: title
#       _#c:
#       - _#r: 应用_用回归图对符号动力学进行半系统的分类_论可测变换或动力系统与度量函数的耦合暨微扰论的拓展
#     - _#t: link
#       _@rel: stylesheet
#       _@href: /theme/css/main.css
#       _#c: []
#     - _#t: link
#       _@href: /feeds/all.atom.xml
#       _@type: application/atom+xml
#       _@rel: alternate
#       _@title: A Pelican Blog Atom Feed
#       _#c: []
s = '''
  - _#t:
      link: _
      rel: stylesheet
      href: /theme/css/main.css
'''
# pprint(ordered_load(s))
# '''
# # import 
# d = ordered_load(s)

# def y(d):
#     pprint([d[0],None])
#     for xx in d[1]:
#       y(xx)
#       # y(d[])
# y(d)
# pprint(d[0])

if __name__=='__main__':
  main()