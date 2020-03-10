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

url="https://zh.moegirl.org/api.php"

params={'action':'query','format':'json','prop':'info','curtimestamp':1,'indexpageids':1}

filepath="PAGELIST.txt"
f=open(filepath,'r',encoding='UTF-8')
pagelistfile=f.read().splitlines()
f.close()

pagelist={}
for line in pagelistfile:
	pagelist[line.split("\t")[2]]=line.split("\t")[1]

pagetitlelist=list(pagelist.keys())

n_all=0
n_moved=0

def devide(l:list,n:int)->list:
	for i in range(0,len(l),n):
		yield l[i:i+n]

def isResponceOK(json:dict)->bool:
	if 'batchcomplete' in json:
		return True
	else:
		print("Responce is not complete.")
		return False

deletedpages=set()

input("Enter to start.")
start_time=time.time()
print("started at",time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(start_time)))

for pagetitlelist_d in devide(pagetitlelist,10):
	l_param:str="|".join(str(i) for i in pagetitlelist_d)
	titleset=set()
	while True:
		try:
			a=requests.get(url,params={**params,**{'titles':l_param}},timeout=(10,30))
		except:
			print(".",end="")
			continue
		else:
			json:dict=a.json()
			break
	if not isResponceOK(json):
		break
	for pageid in json['query']['pageids']:
		if 'missing' in json['query']['pages'][pageid]:
			pass
		else:
			title=json['query']['pages'][pageid]['title']
			if title not in pagelist or pagelist[title]!=pageid:
				print("[MOVED]",pageid,title,sep="\t")
				n_moved+=1
			else:
				print("",pageid,title,sep="\t")
				pass
			n_all+=1
			titleset.add(title)
	deletedpages.update(set(pagetitlelist_d)-titleset)

print()
end_time=time.time()
print("ended   at",time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(end_time)))
print(second2days.main(end_time-start_time),"spent.")
print(len(pagetitlelist),"checked.",n_all,"exist.",n_moved,"moved.")
if len(pagetitlelist)>n_all:
	print("deleted:",deletedpages)

input("Done.")
