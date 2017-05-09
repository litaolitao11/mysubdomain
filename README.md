# subDomainsBrute 1.0.4 #

实例：把百度（baidu.com）的所以子域名找出来，在通过nmap去扫描，得出潜在的
	感染主机

	1,列出百度的所有子域名：
		命令：python subDomainsBrute.py baidu.com > ipaddr_baidu.txt

	2,在通过程序getIP_baidu.py把ipaddr_baidu.txt中的所用ip地址提出来
	
	3,通过nmap命令扫描ipaddr_baidu.txt中的ip地址
		nmap -iL ipaddr_baidu.txt > vuln_port_baidu_submain_name.txt

	4,处理vuln_port_baidu_submain_name.txt文件，找出其中的敏感端口：
		比如： 23, 3389, 3306等等。
		使用vuln_ip_baidu_scan.py可以发现这些端口（因为vuln_port_baidu_submain_name.txt文件条数太多，这样处理一下，就能少了一些。）。

A simple and fast sub domain brute tool for pentesters. It can rearch as fast as 1000 DNS queries per second.

这个脚本的主要目标是发现其他工具无法探测到的域名, 如Google，aizhan，fofa。高频扫描每秒DNS请求数可超过1000次。

## Change Log (Jan 10, 2017) ##
* Add support for extremely huge dict like all 6-letter sub names
* `-t THREADS` could be set, 200 by default

## Change Log (Nov 9, 2016) ##
* Time performance optimization
* Placeholder {alphnum} {alpha} {num} could be used in Names File

## Dependencies ##
First you need to install [dnspython](http://www.dnspython.org/kits/1.12.0/) to do DNS query
> pip install dnspython


## Usage ##

	Usage: subDomainsBrute.py [options] target.com
	
	Options:
	  --version             show program's version number and exit
	  -h, --help            show this help message and exit
	  -f FILE               A file contains new line delimited subs, default is
	                        subnames.txt.
	  --full                Full scan, NAMES FILE subnames_full.txt will be used
	                        to brute
	  -i, --ignore-intranet
	                        Ignore domains pointed to private IPs
	  -t THREADS, --threads=THREADS
	                        Num of scan threads, 200 by default
	  -o OUTPUT, --output=OUTPUT
	                        Output file name. default is {target}.txt


## Screenshot ##
![screenshot](screenshot.png)

Output file could be like: [https://github.com/lijiejie/subDomainsBrute/blob/master/dict/sample_youku.com_full.txt](https://github.com/lijiejie/subDomainsBrute/blob/master/dict/sample_youku.com_full.txt)

LiJieJie my[at]lijiejie.com ([Blog](http://www.lijiejie.com))