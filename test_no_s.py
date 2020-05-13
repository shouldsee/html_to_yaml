# from html_to_yaml import *
from no_s import *
def test_str_html_to_yaml():
  output = '''
_#t: html
_@lang: en
_#c:
- _#t: head
  _#c:
  - _#t: meta
    _@charset: utf-8
    _#c: []
  - _#t: title
    _#c:
    - _#r: 应用_用回归图对符号动力学进行半系统的分类_论可测变换或动力系统与度量函数的耦合暨微扰论的拓展
  - _#t: link
    _@rel: stylesheet
    _@href: /theme/css/main.css
    _#c:
    - _#r: anything
    - _#t: a
      _@href: ''
      _#c:
      - _#r: blah
    - _#r: something
    - _#t: a
      _#c: []
    - _#r: something_else
  - _#t: link
    _@href: /feeds/all.atom.xml
    _@type: application/atom+xml
    _@rel: alternate
    _@title: A Pelican Blog Atom Feed
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
_#t: link
_@rel: stylesheet
_@href: /theme/css/main.css
_#c:
  - _#r: anything
  - {_#t: a, _@href: '', _#cr: blah }
  '''
  exp = '<link rel="stylesheet" href="/theme/css/main.css">anything<a href="">blah</a></link>'
  xd = ordered_load(xx)
  pprint(xd)
  y = str_yaml_to_html(xx)
  assert y==exp,(y,exp)

import yaml
from collections import OrderedDict
