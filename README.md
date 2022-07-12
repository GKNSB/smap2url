## smap2url
Convert smap results to urls. Helper script that takes as input a Lepus resolution file and a .gnmap file from smap and produces a list of URLs. For use when you want passive identification of valid URLs without actually touching the systems in question.

```
usage: smap2url.py [-h] resolutionsFile gnmapFile output

I derive URLs from smap and Lepus

positional arguments:
  resolutionsFile  File containing lepus resolutions results. (e.x. results_public.csv)
  gnmapFile        gnmap file containing portscan results
  output           Output file location

optional arguments:
  -h, --help       show this help message and exit
```
