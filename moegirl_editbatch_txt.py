"""
Python 3.8.0
登录并批量编辑指定页面

Mar 9, 2020
Hu Xiangyou

注意：运行此程序前请务必先测试通过
请优先考虑在提问求助区请求批量替换，而不是擅自对条目进行大幅修改
"""

import moegirl_edit
import requests
import time

print(__doc__)

listPath="PAGELIST.txt"

url="https://zh.moegirl.org/api.php"
USERNAME=YOUR_USERNAME
PASSWORD=YOUR_PASSWORD
moegirl_edit.session=requests.Session()

old=""
new=""

f=open(listPath,'r',encoding='UTF-8')
pagelistfile=f.read().splitlines()
f.close()
pageidlist=[]
for pageline in pagelistfile:
	if pageline.split("\t")[0] in ('[M___]','[T___]','[C___]'):
		pageidlist.append(int(pageline.split("\t")[1]))

n_all=0
n_edited=0
n_error=0

def second2days(seconds:float=0.00)->str:
	"""将秒数转换为时间表述"""
	m,s=divmod(seconds,60)
	h,m=divmod(m,60)
	d,h=divmod(h,24)
	y,d=divmod(d,365)

	y=str(int(y))+" 年" if y else ""
	d=str(int(d))+" 天" if d else ""
	h=str(int(h))+" 小时" if h else ""
	m=str(int(m))+" 分钟" if m else ""
	s=str(round(s,2))+" 秒" if s else ""

	return " ".join(i for i in (y,d,h,m,s) if i)

input("按Enter开始。")
start_time=time.time()
print("开始于",time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(start_time)))

moegirl_edit.login(username=USERNAME,password=PASSWORD)

if old:
	for pageid in pageidlist:
		if n_all and not n_all%10:
			time.sleep(50)
		while True:
			try:
				result=moegirl_edit.replace(pageid=pageid,old=old,new=new)
			except:
				continue
			else:
				break
		n_all+=1
		if result:
			print("[替换]","[√]","[PID]",pageid,sep="\t")
			n_edited+=1
		elif result==False:
			print("[替换]","[失败]","[PID]",pageid,sep="\t")
			n_error+=1
		elif result==None:
			print("[替换]","[-]","[PID]",pageid,sep="\t")

print()
end_time=time.time()
print("结束于",time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(end_time)))
print("耗时",second2days(end_time-start_time))

print(n_all,"个已检查。")
print(n_edited,"个被编辑。",n_error,"个失败。")

input("完成。")
