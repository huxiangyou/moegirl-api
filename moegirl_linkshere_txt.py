"""
Python 3.8.0
列出所有链入到收录的链接的却没有被收录的页面
大约耗时40分钟

Jan 19, 2020
Hu Xiangyou
"""
print(__file__.rsplit("\\",1)[1])
print(__doc__)
import requests
from urllib import parse
import time
import openpyxl
import second2days

url="https://zh.moegirl.org/api.php"

params={'action':'query','format':'json','prop':'linkshere','curtimestamp':1,'indexpageids':1,'lhlimit':500,'lhshow':'!redirect','lhprop':'pageid|title','lhnamespace':'*'}

filepath="PAGELIST.txt"
f=open(filepath,'r',encoding='UTF-8')
pagelistfile=f.read().splitlines()
f.close()
pageidlist=[]
pagetitlelist:list=[]
for pageline in pagelistfile:
	if pageline.split("\t")[0] not in ('',):
		pageidlist.append(int(pageline.split("\t")[1]))
		pagetitlelist.append(pageline.split("\t")[2])

n_all=0
link_new={}
ns2ns={
0:"Main".ljust(14),1:"Talk".ljust(14),
2:"User".ljust(14),3:"User_talk".ljust(14),
4:"Project".ljust(14),5:"Project_talk".ljust(14),
6:"File".ljust(14),7:"File_talk".ljust(14),
8:"MediaWiki".ljust(14),9:"MediaWiki_talk".ljust(14),
10:"Template".ljust(14),11:"Template_talk".ljust(14),
12:"Help".ljust(14),13:"Help_talk".ljust(14),
14:"Category".ljust(14),15:"Category_talk".ljust(14),
274:"Widget".ljust(14),275:"Widget_talk".ljust(14),
710:"TimedText".ljust(14),711:"TimedText_talk".ljust(14),
828:"Module".ljust(14),829:"Module_talk".ljust(14),
2300:"Gadget".ljust(14),2301:"Gadget_talk".ljust(14),
}

def isResponceContinue(json:dict)->bool:
	if 'batchcomplete' in json:
		return json['batchcomplete']
	elif 'continue' in json:
		return json['continue']['lhcontinue']
	else:
		print("[!!] Responce is not complete.")
		return True

pagetitlelinkedfromlist:list=pagetitlelist.copy()

input("Enter to start.")
start_time=time.time()
print("started at",time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(start_time)))

for pagetitle in pagetitlelist:
	lhcontinue=''
	while True:
		while True:
			try:
				if lhcontinue:
					a=requests.get(url,params={**params,**{'titles':pagetitle,'lhcontinue':lhcontinue}},timeout=(10,30))
				else:
					a=requests.get(url,params={**params,**{'titles':pagetitle}},timeout=(10,30))
			except:
				print(".",end="")
				continue
			else:
				break
		json:dict=a.json()
		pageid=int(json['query']['pageids'][0])
		title=json['query']['pages'][str(pageid)]['title']
		if 'linkshere' in json['query']['pages'][str(pageid)]:
			for linkJson in json['query']['pages'][str(pageid)]['linkshere']:
				linktitle=linkJson['title'] if 'title' in linkJson else ""
				linkid=linkJson['pageid'] if 'pageid' in linkJson else ""
				linkns=linkJson['ns'] if 'ns' in linkJson else ""
				if linktitle not in pagetitlelinkedfromlist:
					pagetitlelinkedfromlist.append(linktitle)
					print("[链][外]","\t[Linked]",pageid,"\t",title,"\t[From]",linkid,"\t",linktitle,sep="")
					if linkns in link_new:
						link_new[linkns]+=1
					else:
						link_new[linkns]=1
				else:
					#print("[链][内]","\t[LinkedID]",pageid,"\t[Linked]",title,"\t[From]",linktitle,sep="")
					pass
		lhcontinue=isResponceContinue(json)
		if not lhcontinue:
			break


print()
end_time=time.time()
print("ended   at",time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(end_time)))
print(second2days.main(end_time-start_time),"spent.")

print(sum(link_new.values()),"links found.")
for ns in link_new:
	print("[NS]",ns2ns[ns],"\t[LinkedFrom]",link_new[ns])

input("Done.")
