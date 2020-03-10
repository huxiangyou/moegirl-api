"""
Python 3.8.0
列出所有使用了文件但没有收录的页面
大约耗时15分钟

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

params={'action':'query','format':'json','prop':'fileusage','curtimestamp':1,'indexpageids':1,'fulimit':'max','funamespace':'*'}

n_all=0
n_nouse=0
use_new=0

def devide(l:list,n:int)->list:
	for i in range(0,len(l),n):
		yield l[i:i+n]

def isResponceContinue(json:dict)->bool:
	if 'batchcomplete' in json:
		return json['batchcomplete']
	elif 'continue' in json:
		return json['continue']['lhcontinue']
	else:
		print("[!!] Responce is not complete.")
		return True

file="imagelist.xlsx"

Workbook:type=openpyxl.workbook.workbook.Workbook
Worksheet:type=openpyxl.worksheet.worksheet.Worksheet
Cell:type=openpyxl.cell.cell.Cell

bi:Workbook=openpyxl.load_workbook(file)

imagetitlelist:list=[]
for sheet in bi.worksheets:
	imagetitlelist+=[c.value for c in list(sheet.columns)[2]]

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

input("Enter to start.")
start_time=time.time()
print("started at",time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(start_time)))

for imagetitlelist_d in devide(imagetitlelist,20):
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
	for image in json['query']['pages']:
		imageJson=json['query']['pages'][image]
		imagetitle=imageJson['title']
		if 'fileusage' in imageJson:
			for pageJson in imageJson['fileusage']:
				pagetitle=pageJson['title'] if 'title' in pageJson else ""
				pageid=pageJson['pageid'] if 'pageid' in pageJson else ""
				if pagetitle not in pagetitlelist:
					pagetitlelist.append(pagetitle)
					print("[图用][外]","\t[File]",imagetitle,"\t[Page]",pageid,"\t",pagetitle,sep="")
					use_new+=1
				else:
					#print("[图用][内]","\t[File]",imagetitle,"\t[Page]",pageid,"\t",pagetitle,sep="")
					pass
		else:
			print("[图][没用]","\t[File]",imagetitle,sep="")
			n_nouse+=1


print()
end_time=time.time()
print("ended   at",time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(end_time)))
print(second2days.main(end_time-start_time),"spent.")

print(n_nouse,"files not in use.")
print(use_new,"new pages found using files.")

input("Done.")