#!/usr/bin/env python
import re
import tqdm
from argparse import ArgumentParser, FileType

portsHTTP = ['80', '8080']
portsHTTPS = ['443', '8443']

parser = ArgumentParser(prog="smap2url.py", description="I derive URLs from smap and Lepus")
parser.add_argument("resolutionsFile", help="File containing lepus resolutions results. (e.x. results_public.csv)", type=str)
parser.add_argument("gnmapFile", help="gnmap file containing portscan results", type=str)
parser.add_argument("output", help="Output file location", type=str)
args = parser.parse_args()

URLs = []
counter = 0
LINE_UP = "\033[1A"
LINE_CLEAR = "\x1b[2K"

with open(args.resolutionsFile, "r") as domainsFile:
	resolutions = domainsFile.readlines()
	for domainentry in resolutions:
		domainIPs = []
		domainentry = domainentry.strip()
		domainDomain = domainentry.split("|")[0]
		tmp = domainentry.split("|")[1]
		if "," in tmp:
			domainIPs = tmp.split(",")
		else:
			domainIPs.append(tmp)

		with open(args.gnmapFile, "r") as infile:
			for tmpline in infile:
				line = tmpline.strip()
				if "Nmap" in line:
					pass
				else:
					openports = re.findall("(\d+)\/open", line.strip())
					ip = re.findall("Host:\s(\d+\.\d+\.\d+\.\d+)", line)

					if ip:
						ip = ip[0]
						if openports:
							if ip in domainIPs:
								for openport in openports:
									if openport in portsHTTP:
										URLs.append(f"http://{domainDomain}:{openport}/")
									elif openport in portsHTTPS:
										URLs.append(f"https://{domainDomain}:{openport}/")

		counter += 1
		print(f"Processed: {counter}/{len(resolutions)}")
		if not counter == len(resolutions): print(LINE_UP, end=LINE_CLEAR)

with open(args.output, "w") as outfile:
	for url in list(set(URLs)):
		outfile.write(f"{url}\n")
