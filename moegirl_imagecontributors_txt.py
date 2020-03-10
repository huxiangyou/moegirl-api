"""
Python 3.8.0
找出对指定图片做出过贡献的用户

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

filepath="imagelist.txt"

url="https://common.moegirl.org/api.php"

params={'action':'query','format':'json','prop':'contributors','pclimit':'max','curtimestamp':1,'indexpageids':1}

f=open(filepath,'r',encoding='UTF-8')
pagelistfile=f.read().splitlines()
f.close()
imagetitlelist=[]
for pageline in pagelistfile:
	imagetitlelist.append(pageline)

n_all=0
users={}

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


for imagetitlelist_d in devide(imagetitlelist,10):
	l_param:str="|".join(str(i) for i in imagetitlelist_d)
	while True:
		try:
			a=requests.get(url,params={**params,**{'titles':l_param}},timeout=(10,30))
		except:
			print(".",end="")
			continue
		else:
			break
	json:dict=a.json()
	if not isResponceOK(json):
		break
	for pageid in json['query']['pageids']:
		contributors=[c["name"] for c in json['query']['pages'][str(pageid)]['contributors']]
		title=json['query']['pages'][str(pageid)]['title']
		for c in contributors:
			if c in users:
				users[c]+=1
			else:
				users[c]=1
		print("[编者]","\t[PID]",pageid,"\t[Title]",title,"\t",contributors)
		n_all+=1

print()
end_time=time.time()
print("ended   at",time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(end_time)))
print(second2days.main(end_time-start_time),"spent.")

users_morethan5={}
for i in users:
	if users[i]>=5:
		users_morethan5[i]=users[i]

print(n_all,"pages checked.")
print(len(users),"contributors found.")
print(users_morethan5,len(users_morethan5))

input("Done.")