# pygreynoise

Python 3 wrapper for the greynoise API v1, see https://github.com/Grey-Noise-Intelligence/api.greynoise.io and greynoise.io. API V1 is nor deprecated but still working, see [this project](https://github.com/GreyNoise-Intelligence/pygreynoise) for the API V2

To install, either use pypi with `pip install pygreynoisev1` or install from sources:
```
git clone https://github.com/Te-k/pygreynoisev1.git
cd pygreynoisev1
pip install -r requirements.txt
pip install .
```

## CLI

```
$ greynoisev1 -h
usage: greynoise [-h] {ip,list,tag,config} ...

Request GreyNoise

positional arguments:
  {ip,list,tag,config}  Subcommand
    ip                  Request info on an IP
    list                List GreyNoise Tags
    tag                 Query data for a tag
    config              Configure key file

optional arguments:
  -h, --help            show this help message and exit
```

## Library

```python
from pygreynoisev1 import GreyNoise

gn = GreyNoise()
tags = gn.tags()

try:
    gn.query_ip('198.20.69.74')
except GreyNoiseError:
    print('IP not found')

try:
    gn.query_tag('YANDEX_SEARCH_ENGINE')
except GreyNoiseError:
    print('This tag does not exist')
```

## Author and license

Pygreynoisev1 was started by [Tek](https://github.com/Te-k) and is published under MIT license. Feel free to open issues and pull requests.
