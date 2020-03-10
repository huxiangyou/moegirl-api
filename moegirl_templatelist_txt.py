"""
Python 3.8.0
列出页面中包含的所有没有收录的模板
大约耗时40分钟

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

params={'action':'query','format':'json','prop':'templates','curtimestamp':1,'indexpageids':1,'tllimit':500}

filepath="PAGELIST.txt"
f=open(filepath,'r',encoding='UTF-8')
pagelistfile=f.read().splitlines()
f.close()
pageidlist={}
pagetitlelist={}
pagetitlelistall=[]
for pageline in pagelistfile:
	attr=pageline.split("\t")[0]
	if attr in pageidlist:
		pageidlist[attr].append(int(pageline.split("\t")[1]))
	else:
		pageidlist[attr]=[int(pageline.split("\t")[1])]
	pagetitlelistall.append(pageline.split("\t")[2])

n_all=0
template_new={}
for attr in pageidlist:
	pagetitlelist[attr]=pagetitlelistall.copy()
	template_new[attr]=0
template_new_all=0

def isResponceOK(json:dict)->bool:
	if 'batchcomplete' in json:
		return True
	else:
		print("Responce is not complete.")
		return False

input("Enter to start.")
start_time=time.time()
print("started at",time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(start_time)))

for attr in pageidlist:
	for pageid in pageidlist[attr]:
		while True:
			try:
				a=requests.get(url,params={**params,**{'pageids':pageid}},timeout=(10,30))
			except:
				print(".",end="")
				continue
			else:
				break
		json:dict=a.json()
		if not isResponceOK(json):
			break
		if 'templates' in json['query']['pages'][str(pageid)]:
			for templateJson in json['query']['pages'][str(pageid)]['templates']:
				templateTitle=templateJson['title'] if 'title' in templateJson else ""
				if templateTitle not in pagetitlelist[attr]:
					pagetitlelist[attr].append(templateTitle)
					print("[用][模板]\t",attr,"\t[PID]",pageid,"\t[Template]",templateTitle)
					template_new[attr]+=1
				else:
					#print("-\t\t",attr,"\t[PID]",pageid,"\t[Template]",templateTitle)
					pass
				if templateTitle not in pagetitlelistall:
					pagetitlelistall.append(templateTitle)
					#print("[用][模板]\t",attr,"\t[PID]",pageid,"\t[Template]",templateTitle)
					template_new_all+=1
				else:
					#print("-\t\t",attr,"\t[PID]",pageid,"\t[Template]",templateTitle)
					pass

print()
end_time=time.time()
print("ended   at",time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(end_time)))
print(second2days.main(end_time-start_time),"spent.")

print(template_new_all,"templates used in those pages.")
for attr in template_new:
	print(attr,"\t[Template]",template_new[attr])

input("Done.")