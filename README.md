# uri_safe

A tool to de-fang or re-arm malicious urls.

### Usage

```
usage: uri_safe.py [-h] [--defang DEFANG] [--rearm REARM]

options:
  -h, --help       show this help message and exit
  --defang DEFANG  python3 uri_safe.py --defang 'http://exemple.com'
  --rearm REARM    python3 uri_safe.py --rearm 'hXXp[:]//exmple[.]com'
```

### URI support

Supports the following protocol URI schemes:  
https://www.iana.org/assignments/uri-schemes/uri-schemes.xhtml  
https://en.wikipedia.org/wiki/List_of_URI_schemes  
