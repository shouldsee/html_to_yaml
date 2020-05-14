
# html_to_yaml

## Overview

### Motivation:

Indentation is more intuitive to human than paired brakets, hence an
indented data representation would help debugging and editing website.

### Treatment of DTD:

Doctype/DTD implicitly configures the behaviour of lxml parsing. Thus xml with different
doctype strings should be defined on the (D)ocument basis by specifying a header containing
public_id and system_url. 

To enable HTML entities, add the following doctype specifier. Note 
this might alter document recoverbility


```yaml
_: D
doctype:
  public_id: -//W3C//DTD HTML 4.01//EN
  system_url: http://www.w3.org/TR/html4/strict.dtd
_#c:
- html: T
```

The xml equivalent being

```xml
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
```



If both set to null or unspecified, then we use no DTD and assuming the document is pure XML
without comments, whitespaces or numbered entities. 

```yaml
_: D
_#c:
- html: T
```

```yaml
_: D
public_id: null
system_url: null
_#c:
- html: T
```

### Regex for Common HTML error

```
&([^ag]) -> &amp;

</br> <br> -> <br/>
```
