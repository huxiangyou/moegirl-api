"""
Python 3.8.0
列出所有使用了模板但没有收录的页面
大约耗时1分钟

Jan 19, 2020
Hu Xiangyou
"""
print(__file__.rsplit("\\",1)[1])
print(__doc__)
import requests
from urllib import parse
import time
import second2days

url="https://zh.moegirl.org/api.php"

params={'action':'query','format':'json','prop':'transcludedin','curtimestamp':1,'indexpageids':1,'tilimit':'max','tinamespace':'*'}

n_all=0
use_new=0

def isResponceContinue(json:dict)->bool:
	if 'continue' in json:
		return json['continue']['ticontinue']
	else:
		return ""

filepath="PAGELIST.txt"
f=open(filepath,'r',encoding='UTF-8')
pagelistfile=f.read().splitlines()
f.close()
pageidlist=[]
pagetitlelist:list=[]
for pageline in pagelistfile:
	if pageline.split("\t")[0] in ('[T___]',):
		pageidlist.append(int(pageline.split("\t")[1]))
		pagetitlelist.append(pageline.split("\t")[2])
pagelinkedfromidlist=pageidlist.copy()
for pageline in pagelistfile:
	pagelinkedfromidlist.append(int(pageline.split("\t")[1]))

input("Enter to start.")
start_time=time.time()
print("started at",time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(start_time)))

for templateid in pageidlist:
	ticontinue=''
	while True:
		while True:
			try:
				if ticontinue:
					a=requests.get(url,params={**params,**{'pageids':templateid,'ticontinue':ticontinue}},timeout=(10,30))
				else:
					a=requests.get(url,params={**params,**{'pageids':templateid}},timeout=(10,30))
			except:
				print(".",end="")
				continue
			else:
				break
		json:dict=a.json()
		templatetitle=json['query']['pages'][str(templateid)]['title']
		if 'transcludedin' in json['query']['pages'][str(templateid)]:
			for pageJson in json['query']['pages'][str(templateid)]['transcludedin']:
				pagetitle=pageJson['title'] if 'title' in pageJson else ""
				pageid=pageJson['pageid'] if 'pageid' in pageJson else ""
				if pageid not in pagelinkedfromidlist:
					pagelinkedfromidlist.append(pageid)
					print("[模用][外]","\t[Temp]",templateid,"\t",templatetitle,"\t[Page]",pageid,"\t",pagetitle,sep="")
					use_new+=1
				else:
					#print("[模用][内]","\t[Temp]",templateid,"\t",templatetitle,"\t[Page]",pageid,"\t",pagetitle,sep="")
					pass
		ticontinue=isResponceContinue(json)
		if not ticontinue:
			break


print()
end_time=time.time()
print("ended   at",time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(end_time)))
print(second2days.main(end_time-start_time),"spent.")

print(use_new,"new pages found using templates.")

input("Done.")