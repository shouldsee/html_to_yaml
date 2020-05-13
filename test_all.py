# from html_to_yaml import *
# from no_s import *
from html_to_yaml import *
def test_str_html_to_yaml():
  output = '''
html: _
lang: en
_#c:
- head: _
  _#c:
  - meta: _
    charset: utf-8
    _#c: []
  - title: _
    _#c:
    - 应用_用回归图对符号动力学进行半系统的分类_论可测变换或动力系统与度量函数的耦合暨微扰论的拓展
  - link: _
    rel: stylesheet
    href: /theme/css/main.css
    _#c:
    - anything
    - a: _
      href: ''
      _#c:
      - blah
    - something
    - a: _
      _#c: []
    - something_else
  - link: _
    href: /feeds/all.atom.xml
    type: application/atom+xml
    rel: alternate
    title: A Pelican Blog Atom Feed
    _#c: []
'''.strip()
  x = yaml.load(output)
  pprint(x)

  input = (
  # '<?xml version="1.0" encoding="utf-8"?>\n'
 '<html lang="en"><head><meta '
 'charset="utf-8"/><title>应用_用回归图对符号动力学进行半系统的分类_论可测变换或动力系统与度量函数的耦合暨微扰论的拓展</title><link '
 'rel="stylesheet" href="/theme/css/main.css">'
 'anything<a href="">blah</a>something<a/>something_else'
 '</link>'
 '<link '
 'href="/feeds/all.atom.xml" type="application/atom+xml" rel="alternate" '
 'title="A Pelican Blog Atom Feed"/></head></html>')
  ET.fromstring(input)
  # pprint(xmltodict.unparse(xmltodict.parse(input)))

  # assert 0
  y = str_html_to_yaml(input)
  y = y.strip().splitlines()
  x = output.strip().splitlines()
  assert x==y,pprint(list([(a,b,a==b) for a,b in zip(x,y)]))



  # yd = yaml.safe_load('\n'.join(y))
  xx = str_yaml_to_html('\n'.join(y))
  xx = xx.split('<') 
  yy = input.split('<')
  assert xx==yy, pprint([(a,b,a==b) for a,b,in zip(xx,yy)])
  # ,output.splitlines())))
  # print(x)
def test_inline():
  xx = '''
link: _
rel: stylesheet
href: /theme/css/main.css
_#c:
  - anything
  - {a: _, href: '', _#cr: blah }
  '''
  exp = '<link rel="stylesheet" href="/theme/css/main.css">anything<a href="">blah</a></link>'
  xd = ordered_load(xx)
  pprint(xd)
  y = str_yaml_to_html(xx)
  assert y==exp,(y,exp)

import yaml
from collections import OrderedDict
