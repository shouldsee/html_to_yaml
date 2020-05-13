# from html_to_yaml import *
# from no_s import *
from html_to_yaml import *
def test_str_html_to_yaml():

  input = (

  # '<?xml version="1.0" encoding="utf-8"?>'
  # '<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"  "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">\n'
 # '<!DOCTYPE html>\n'
 '<html lang="en"><head><meta '
 'charset="utf-8"/>'
 '<title>应用_用回归图对符号动力学进行半系统的分类_论可测变换或动力系统与度量函数的耦合暨微扰论的拓展</title><link '
 'rel="stylesheet" href="/theme/css/main.css">'
 'anything<a href="">blah</a>something<a/>'
 ## numbered entity is dangerous!!!
 # '&#60;something&nbsp;else'
 '</link>'
 '<link '
 'href="/feeds/all.atom.xml" type="application/atom+xml" rel="alternate" '
 'title="A Pelican Blog Atom Feed"/></head></html>'
 )
  # x = str_html_to_yaml(input)
  # assert 0,x
  # (x.splitlines())
  _test_xml_recover(input)

  input = (

  # '<?xml version="1.0" encoding="utf-8"?>'
  # '<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"  "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">\n'
 '<!DOCTYPE html>\n'
 '<html lang="en"><head><meta '
 'charset="utf-8"/>'
 '<title>应用_用回归图对符号动力学进行半系统的分类_论可测变换或动力系统与度量函数的耦合暨微扰论的拓展</title><link '
 'rel="stylesheet" href="/theme/css/main.css">'
 'anything<a href="">blah</a>something<a/>'
 ## numbered entity is dangerous!!!
 # '&#60;something&nbsp;else'
 '</link>'
 '<link '
 'href="/feeds/all.atom.xml" type="application/atom+xml" rel="alternate" '
 'title="A Pelican Blog Atom Feed"/></head></html>')
  # x = str_html_to_yaml(input)
  # assert 0,x
  # (x.splitlines())
  _test_xml_recover(input)



  output = '''
_: D
_#c:
- html: T
  lang: en
  _#c:
  - head: T
    _#c:
    - meta: T
      charset: utf-8
      _#c: []
    - title: T
      _#c:
      - 应用_用回归图对符号动力学进行半系统的分类_论可测变换或动力系统与度量函数的耦合暨微扰论的拓展
    - link: T
      rel: stylesheet
      href: /theme/css/main.css
      _#c:
      - anything
      - a: T
        href: ''
        _#c:
        - blah
      - <something
      - a: T
        _#c: []
      - something_else
    - link: T
      href: /feeds/all.atom.xml
      type: application/atom+xml
      rel: alternate
      title: A Pelican Blog Atom Feed
      _#c: []
'''.strip()
  x = yaml.load(output)
  pprint(x)
  _test_yaml_recover(output)

  output = '''
_: D
doctype:
  public_id: -//W3C//DTD HTML 4.01 Transitional//EN
  system_url: http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd
_#c:
- html: T
  '{http://www.w3.org/1999/xhtml}lang': en
  _#c:
  - '{http://www.w3.org/1999/xhtml}head': T
    _#c:
    - '{http://www.w3.org/1999/xhtml}meta': T
      http-equiv: Content-Type
      content: text/html; charset=utf-8
      _#c: []
    - '{http://www.w3.org/1999/xhtml}title': T
      _#c:
      - 应用_用回归图对符号动力学进行半系统的分类_论可测变换或动力系统与度量函数的耦合暨微扰论的拓展
    - '{http://www.w3.org/1999/xhtml}link': T
      rel: stylesheet
      href: /theme/css/main.css
      _#c:
      - anything
      - '{http://www.w3.org/1999/xhtml}a': T
        href: ''
        _#c:
        - blah
      - something
      - '{http://www.w3.org/1999/xhtml}a': T
        _#c: []
      - <something
      - nbsp: E
        _#c: []
      - else
    - '{http://www.w3.org/1999/xhtml}link': T
      href: /feeds/all.atom.xml
      type: application/atom+xml
      rel: alternate
      title: A Pelican Blog Atom Feed
      _#c: []
'''.strip()
  _test_yaml_recover(output)

  output = '''
_: D
doctype:
  public_id: -//W3C//DTD HTML 4.01//EN
  system_url: http://www.w3.org/TR/html4/strict.dtd
_#c:
- html: T
  lang: en
  _#c:
  - head: T
    _#c:
    - meta: T
      http-equiv: Content-Type
      content: text/html; charset=utf-8
      _#c: []
    - title: T
      _#c:
      - 应用_用回归图对符号动力学进行半系统的分类_论可测变换或动力系统与度量函数的耦合暨微扰论的拓展
    - link: T
      rel: stylesheet
      href: /theme/css/main.css
      _#c:
      - anything
      - a: T
        href: ''
        _#c:
        - blah
      - something
      - a: T
        _#c: []
      - <something
      - nbsp: E
        _#c: []
      - else
    - link: T
      href: /feeds/all.atom.xml
      type: application/atom+xml
      rel: alternate
      title: A Pelican Blog Atom Feed
      _#c: []
'''.strip()
  _test_yaml_recover(output)

  input = (

  # '<?xml version="1.0" encoding="utf-8"?>'
  # '<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"  "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">\n'
 # '<!DOCTYPE html>\n'
 # '<html lang="en">'
 '<head><meta '
 'charset="utf-8"/>'
 '<title>应用_用回归图对符号动力学进行半系统的分类_论可测变换或动力系统与度量函数的耦合暨微扰论的拓展</title><link '
 'rel="stylesheet" href="/theme/css/main.css">'
 'anything<a href="">blah</a>something<a/>'
 ## numbered entity is dangerous!!!
 # '&#60;something&nbsp;else'
 '</link>'
 '<link '
 'href="/feeds/all.atom.xml" type="application/atom+xml" rel="alternate" '
 'title="A Pelican Blog Atom Feed"/></head>'
 # '</html>'
 )
  _test_xml_recover(input)

  input = (

  # '<?xml version="1.0" encoding="utf-8"?>'
  # '<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"  "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">\n'
 '<!DOCTYPE html>\n'
 '<html lang="en"><head><meta '
 'charset="utf-8"/>'
 '<title>应用_用回归图对符号动力学进行半系统的分类_论可测变换或动力系统与度量函数的耦合暨微扰论的拓展</title><link '
 'rel="stylesheet" href="/theme/css/main.css">'
 'anything<a href="">blah</a>something<a/>'
 ## numbered entity is dangerous!!!
 # '&#60;something&nbsp;else'
 '</link>'
 '<link '
 'href="/feeds/all.atom.xml" type="application/atom+xml" rel="alternate" '
 'title="A Pelican Blog Atom Feed"/></head></html>')
  # x = str_html_to_yaml(input)
  # assert 0,x
  # (x.splitlines())
  _test_xml_recover(input)



  input_out = (

  # '<?xml version="1.0" encoding="utf-8"?>'
  '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">'
  # '<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"  "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">\n'
 '<html lang="en"><head><meta '
 'charset="utf-8" />'
 '<title>应用_用回归图对符号动力学进行半系统的分类_论可测变换或动力系统与度量函数的耦合暨微扰论的拓展</title><link '
 'rel="stylesheet" href="/theme/css/main.css">'
 'anything<a href="">blah</a>something<a></a>'
 ## numbered entity is dangerous!!!
 '&lt;something&nbsp;else'
 '</link>'
 '<link '
 'href="/feeds/all.atom.xml" type="application/atom+xml" rel="alternate" '
 'title="A Pelican Blog Atom Feed" /></head></html>')  


  input_out = (

  # '<?xml version="1.0" encoding="utf-8"?>'
  '<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"  "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">\n'
 '<html lang="en"><head><meta '
 'charset="utf-8" />'
 '<title>应用_用回归图对符号动力学进行半系统的分类_论可测变换或动力系统与度量函数的耦合暨微扰论的拓展</title><link '
 'rel="stylesheet" href="/theme/css/main.css">'
 'anything<a href="">blah</a>something<a></a>'
 ## numbered entity is dangerous!!!
 '&lt;something&nbsp;else'
 '</link>'
 '<link '
 'href="/feeds/all.atom.xml" type="application/atom+xml" rel="alternate" '
 'title="A Pelican Blog Atom Feed" /></head></html>')  

  _ = '''
  Problem
  -----------------------
  Entity is supported through doctype declaration. However, the declared doctype configure the lxml parser to be 
  non-reversible. e.g. it adds content and charset to the <meta> tag. 
  This is very bad.... Because DTD adds information and preset to a structure. 
  Becuase this program should deal with raw xml as well as variants like html, I need to allow user to specify the DTD.
  DTD declares the type of the document. If undeclared, raw xml is assumed.

  It's good to have a reference to the dtd Current decision is to manually decoding entities instead of 
  '''
  _test_xml_recover(input)



  # # ET.fromstring(input)
  # # pprint(xmltodict.unparse(xmltodict.parse(input)))

  # # assert 0
  # y = str_html_to_yaml(input)
  # y = y.strip().splitlines()
  # x = output.strip().splitlines()
  # assert x==y,pprint(list([(a,b,a==b) for a,b in zip(x,y)]))



  # # yd = yaml.safe_load('\n'.join(y))
  # xx = str_yaml_to_html('\n'.join(y))
  # xx = xx.split('<') 
  # yy = input_out.split('<')
  # assert xx==yy, pprint([(a,b,a==b) for a,b,in zip(xx,yy)])
  # # ,output.splitlines())))
  # # print(x)
def _test_yaml_recover(input, output = None):
  if output is None:
    output = input
  x = input
  x = str_yaml_to_html(x)
  # import pdb; pdb.set_trace()
  x = str_html_to_yaml(x)
  assert x.splitlines() == output.splitlines()
  return 0

def _test_xml_recover( input, input_out=None):
  y = str_html_to_yaml(input)
  xx = str_yaml_to_html(y)
  if input_out is  None:
    input_out = input
  assert xx.split('<')==input_out.split('<')
  return 0

def test_inline():
  xx = '''
link: T
rel: stylesheet
href: /theme/css/main.css
_#c:
  - anything
  - {a: T, href: '', _#cr: blah }
  '''
  exp = '<link rel="stylesheet" href="/theme/css/main.css">anything<a href="">blah</a></link>'
  xd = ordered_load(xx)
  pprint(xd)
  y = str_yaml_to_html(xx)
  assert y==exp,(y,exp)

import yaml
from collections import OrderedDict
