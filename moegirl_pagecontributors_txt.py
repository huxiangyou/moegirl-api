"""
Python 3.8.0
找到所有对指定页面做出过贡献的用户

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

url="https://zh.moegirl.org/api.php"

params={'action':'query','format':'json','prop':'contributors','pclimit':'max','curtimestamp':1,'indexpageids':1}

f=open(filepath,'r',encoding='UTF-8')
pagelistfile=f.read().splitlines()
f.close()
pageidlist=[]
for pageline in pagelistfile:
	if pageline.split("\t")[0] in ('[M___]','[T___]','[C___]'):
		pageidlist.append(int(pageline.split("\t")[1]))

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

for pageid in pageidlist:
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
	contributors=json['query']['pages'][str(pageid)]['contributors']
	title=json['query']['pages'][str(pageid)]['title']
	for c in contributors:
		if c["name"] in users:
			users[c["name"]]+=1
		else:
			users[c["name"]]=1
	print("[编者数]","\t[PID]",pageid,"\t[Ctrbtrs]",len(contributors),"\t[Title]",title)
	n_all+=1

print()
end_time=time.time()
print("ended   at",time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(end_time)))
print(second2days.main(end_time-start_time),"spent.")

users_morethan5={}
for i in sorted(users.items(),key=lambda x:x[1],reverse=True):
	if i[1]>=5:
		users_morethan5[i[0]]=users[i[0]]

print(n_all,"pages checked.")
print(len(users),"contributors found.")
print(users_morethan5,len(users_morethan5))

input("Done.")