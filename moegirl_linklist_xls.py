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

filepath="PAGELIST.xlsx"
file="./imagelist.txt"

url="https://zh.moegirl.org/api.php"

params={'action':'query','format':'json','prop':'links','curtimestamp':1,'indexpageids':1,'pllimit':500,'plnamespace':'0|10|14','pageids':''}

Workbook:type=openpyxl.workbook.workbook.Workbook
Worksheet:type=openpyxl.worksheet.worksheet.Worksheet
Cell:type=openpyxl.cell.cell.Cell

b:Workbook=openpyxl.load_workbook(filepath)
sMain:Worksheet=b.worksheets[0]
sTemp:Worksheet=b.worksheets[1]
sCate:Worksheet=b.worksheets[2]
sheets:Worksheet=b.worksheets

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
pageidlist:list=[]
for sheet in sheets:
	pageidlist+=[c.value for c in list(sheet.columns)[1]]

pagetitlelist:list=[]
for sheet in sheets:
	pagetitlelist+=[c.value for c in list(sheet.columns)[3]]
	for c in list(sheet.columns)[5]:
		if c.value:
			pagetitlelist+=list(eval(c.value))

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