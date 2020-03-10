"""
Python 3.8.0
对列出的页面的大小求和

Jan 7, 2020
Jan 15, 2020
Jan 26, 2020
Hu Xiangyou
"""
print(__file__.rsplit("\\",1)[1])
print(__doc__)
import requests
import time
import os
import second2days

filepath="PAGELIST.txt"
fold="archive/"
fileData="!.txt"

url="https://zh.moegirl.org/api.php"

params={'action':'query','format':'json','prop':'info','curtimestamp':1,'indexpageids':1}

f=open(filepath,'r',encoding='UTF-8')
pagelistfile=f.read().splitlines()
f.close()
pageidlist={}
for pageline in pagelistfile:
	attr=pageline.split("\t")[0]
	pageid=pageline.split("\t")[1]
	if attr in pageidlist:
		pageidlist[attr].append(int(pageline.split("\t")[1]))
	else:
		pageidlist[attr]=[pageid]

n_all={}
size_all={}
for attr in pageidlist:
	n_all[attr]=0
	size_all[attr]=0

f=open(fold+fileData,'r',encoding='UTF-8')
reviddict=eval(f.read())
f.close()

def devide(l:list,n:int)->list:
	for i in range(0,len(l),n):
		yield l[i:i+n]

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
	for pageidlist_d in devide(pageidlist[attr],50):
		l_param:str="|".join(str(i) for i in pageidlist_d)
		while True:
			try:
				a=requests.get(url,params={**params,**{'pageids':l_param}},timeout=(10,30))
			except:
				print(".",end="")
				continue
			else:
				break
		json:dict=a.json()
		if not isResponceOK(json):
			break
		for pageid in pageidlist_d:
			if 'missing' in json['query']['pages'][str(pageid)]:
				print(attr,"\t[PID]",pageid,"\t[Ｘ]")
			else:
				size=json['query']['pages'][str(pageid)]['length']
				title=json['query']['pages'][str(pageid)]['title']
				size_all[attr]+=size
				print(attr,"\t[PID]",pageid,"\t[Size]",size,"\t[Title]",title)
				n_all[attr]+=1

print()
end_time=time.time()
print("ended   at",time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(end_time)))
print(second2days.main(end_time-start_time),"spent.")

print(sum(n_all.values()),"pages checked.")
print(sum(size_all.values()),"bytes in total.")
for attr in n_all:
	print(attr,"\t[Pages]",n_all[attr],"\t[Size]",size_all[attr])

input("Done.")