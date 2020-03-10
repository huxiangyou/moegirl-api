"""
Python 3.8.0
列出页面中包含的所有没有收录的链接
大约耗时30分钟

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

params={'action':'query','format':'json','prop':'links','curtimestamp':1,'indexpageids':1,'pllimit':500,'plnamespace':'0','pageids':''}

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

imagepath="imagelist.txt"
f=open(imagepath,'r',encoding='UTF-8')
imagelistfile=f.read().splitlines()
f.close()
pagetitlelist+=imagelistfile

n_all=0
link_new=0

def isResponceContinue(json:dict)->bool:
	if 'batchcomplete' in json:
		return json['batchcomplete']
	elif 'continue' in json:
		return json['continue']['plcontinue']
	else:
		print("[!!] Responce is not complete.")
		return True

input("Enter to start.")
start_time=time.time()
print("started at",time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(start_time)))

for pageid in pageidlist:
	plcontinue=''
	while True:
		while True:
			try:
				if plcontinue:
					a=requests.get(url,params={**params,**{'pageids':pageid,'plcontinue':plcontinue}},timeout=(10,30))
				else:
					a=requests.get(url,params={**params,**{'pageids':pageid}},timeout=(10,30))
			except:
				print(".",end="")
				continue
			else:
				break
		json:dict=a.json()
		title=json['query']['pages'][str(pageid)]['title']
		if 'links' in json['query']['pages'][str(pageid)]:
			for linkJson in json['query']['pages'][str(pageid)]['links']:
				linktitle=linkJson['title'] if 'title' in linkJson else ""
				if linktitle not in pagetitlelist:
					pagetitlelist.append(linktitle)
					print("[链]","\t[PID]",pageid,"\t[Title]",title,"\t[Link]",linktitle)
					link_new+=1
				else:
					#print("-","\t[PID]",pageid,"\t[Link]",linktitle)
					pass
		plcontinue=isResponceContinue(json)
		if not plcontinue:
			break


print()
end_time=time.time()
print("ended   at",time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(end_time)))
print(second2days.main(end_time-start_time),"spent.")

print(link_new,"links found.")

input("Done.")
