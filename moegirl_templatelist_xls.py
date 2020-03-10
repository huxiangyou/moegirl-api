"""
Python 3.8.0
列出页面中包含的所有没有收录的模板
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
sheetnames=["主","Template","Category"]

url="https://zh.moegirl.org/api.php"

params={'action':'query','format':'json','prop':'templates','curtimestamp':1,'indexpageids':1,'tllimit':500,'pageids':''}

Workbook:type=openpyxl.workbook.workbook.Workbook
Worksheet:type=openpyxl.worksheet.worksheet.Worksheet
Cell:type=openpyxl.cell.cell.Cell

b:Workbook=openpyxl.load_workbook(filepath)
sMain:Worksheet=b.worksheets[0]
sTemp:Worksheet=b.worksheets[1]
sCate:Worksheet=b.worksheets[2]
sheets:Worksheet=b.worksheets

n_all=0
template_new=0

def isResponceOK(json:dict)->bool:
	if 'batchcomplete' in json:
		return True
	else:
		print("Responce is not complete.")
		return False
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
			if templateTitle not in pagetitlelist:
				pagetitlelist.append(templateTitle)
				print("[用][模板]","\t[PID]",pageid,"\t[Template]",templateTitle)
				template_new+=1
			else:
				#print("-","\t[PID]",pageid,"\t[Link]",templateTitle)
				pass

print()
end_time=time.time()
print("ended   at",time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(end_time)))
print(second2days.main(end_time-start_time),"spent.")

print(template_new,"templates used in those pages.")

input("Done.")