#-*- coding:utf-8 -*-
"""
Python 3.8.0
列出指定用户编辑的但没有收录的图片
大约耗时40分钟

Jan 29, 2020
Hu Xiangyou
"""
print(__file__.rsplit("\\",1)[1])
print(__doc__)
import requests
from urllib import parse
import time
import openpyxl
import second2days

url="https://common.moegirl.org/api.php"

params={'action':'query','format':'json','list':'usercontribs','curtimestamp':1,'indexpageids':1,'uclimit':'max','ucnamespace':'6','ucprop':'timestamp|ids|title'}

user_all=0
image_new=0

def isResponceOK(json:dict)->bool:
	if 'batchcomplete' in json:
		return True
	else:
		print("Responce is not complete.")
		return False

def isResponceContinue(json:dict)->bool:
	if 'continue' in json:
		return json['continue']['uccontinue']
	else:
		return False

filepath="imagelist.xlsx"

Workbook:type=openpyxl.workbook.workbook.Workbook
Worksheet:type=openpyxl.worksheet.worksheet.Worksheet
Cell:type=openpyxl.cell.cell.Cell

b:Workbook=openpyxl.load_workbook(filepath)
sheets:Worksheet=b.worksheets

imageidlist:list=[]
imagetitlelist:list=[]
for sheet in sheets:
	imageidlist+=[c.value for c in list(sheet.columns)[1]]
	imagetitlelist+=[c.value for c in list(sheet.columns)[2]]

usernamelist1={
#'安迪布兰顿大人': 104,
#'CFSO6459': 255,
#'Xuanfengsaoye': 25,
'库特莉亚芙卡2': 57,
'Recital君': 184,
'Eddie32': 304,
'Concon': 34,
'红魔狗头人': 130,
#'萌百娘的胖次': 136,
'Bxxiaolin': 38,
'Hamon002': 154,
#'AnnAngela': 187,
'萌爹百科': 28,
'JurinaMiyuki': 115,
#'可爱的琉璃月': 289,
'胡祥又': 547,
'Niconicozha': 183,
#'宇文天启': 21,
'Silver Sulfate': 56,
'樱内夜羽': 29,
'Hooonooka': 31,
'MHCNMLGBD': 25,
'Yumeto': 280,
#'泡泡糖公主': 118,
'花生仔': 258,
'世界第三果厨': 201,
'魔刀祖师': 25,
'花阳使我快乐': 50,
#'一枚颜艺君': 41,
'Fukuisim': 37,
'Swingcosmic': 52,
'FITZGERALD': 45,
'Iloveses': 45,
'BrianYuH750': 45,
'Awd1242': 151,
#'Baskice': 23,
'MagaFun': 28,
#'妹空酱': 25,
'Qwetional': 23,
#'弗霖凯': 77,
'BlackHerrey': 40,
#'蓝羽汇': 47,
'HOOCCOOH': 51,
#'Zyksnowy': 39,
#'W3jc': 115,
'Liutiecheng1999': 62,
#'Shirrak': 89,
#'MERCCCP': 38,
'MuLin': 44,
'Colorless wind': 130,
#'Nostalgia': 30,
'D41D8CD98F': 20,
#'猫耳南云霞': 20,
'Zyzsdy': 70,
#'喵伯爵': 20,
'小火龙6699': 29,
'小铃酱': 27,
'Yangxu76758564': 47,
'正规空母翔鹤改': 240,
#'T.E.Zimmern': 100,
'白学家羊驼': 54,
'17orAvril': 312,
'Chazeon': 61,
'KotoriBee': 87,
'Silverpearl': 82,
'Kitou Akari': 54,
'Miro Winston': 136,
'Masanaga': 160,
'四月夏至': 51,
'非鱼': 28,
'Dqsxc01': 129,
'Pp9101': 36,
'あるゆな': 81,
'朱容稷': 105,
'B777300er': 32,
'颢气泠然': 45,
'安梦': 45,
'Solidgreen02': 160,
'123ysg': 213,
'HoshinoSaika': 65,
#'在下比利有何贵干': 27,
'冬青月': 48,
'Bhsd': 84,
'Qwe20100302': 23,
'Gzfantasy': 23,
'Yinbombs': 20,
'A1013435344': 26,
'Bob1301': 55,
'Cyclo': 71,
'派派': 26,
'Killprince': 25,
'Qscdefb': 69,
'你这里是不是有问题': 29,
'Jmblb233': 35,
'Jlty6273k': 23,
'神百小黄': 23,
'Stylish me': 75,
'Shatterme': 95,
'小鸟厨东酱': 45,
'Kana Ce722419': 40,
'Chikachi': 29,
'Hanamarumaru': 27,
'Lsrxzz000': 29}

usernamelist2={'Eddie32': 285,
'胡祥又': 1812,
'Hamon002': 42,
#'猫耳南云霞': 83,
'Recital君': 24,
'秋名山爱抖露': 10,
#'泡泡糖公主': 1652,
'花生仔': 184,
#'Shirrak': 478,
'17orAvril': 1582,
'红魔狗头人': 123,
'Concon': 10,
#'CFSO6459': 14,
#'蓝羽汇': 143,
#'AYAegis': 5,
'Liutiecheng1999': 8,
'世界第三果厨': 48,
#'Nostalgia': 7,
#'可爱的琉璃月': 96,
#'W3jc': 29,
#'卫宫': 8,
'EliAyase': 6,
'DF5-1310': 6,
'HoshinoSaika': 529,
#'平塚八兵衛': 7,
'BrianYuH750': 11,
'Wingyintang': 6,
'斯大王': 12,
'Solidgreen02': 7,
'Lsrxzz000': 190,
'正规空母翔鹤改': 74,
'达鲁谷': 9,
#'Zyksnowy': 13,
'Cyclo': 11,
'Stylish me': 16,
'Yangxu76758564': 6,
'冬青月': 230,
'Miro Winston': 211,
'Shatterme': 310,
'Yumeto': 16,
'CidDiaz': 10,
'偷星地铁': 5,
#'宫本美代子': 7,
'Nickdoth': 5,
'屠心': 6,
'Swingcosmic': 6,
#'一枚颜艺君': 5,
'Wjl2wjl2': 18,
#'安迪布兰顿大人': 14,
'我是谁无名氏': 37,
'Zyzsdy': 6,
'Bhsd': 11,
'Masanaga': 78,
'CNVNM': 5,
'向晚生凉': 9}

usernamelist=set(usernamelist1.keys())|set(usernamelist2.keys())

input("Enter to start.")
start_time=time.time()
print("started at",time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(start_time)))

for username in usernamelist:
	uccontinue=''
	while True:
		while True:
			try:
				if uccontinue:
					a=requests.get(url,params={**params,**{'ucuser':username,'uccontinue':uccontinue}},timeout=(10,30))
				else:
					a=requests.get(url,params={**params,**{'ucuser':username}},timeout=(10,30))
			except:
				print(".",end="")
				continue
			else:
				break
		json:dict=a.json()
		for contribJson in json['query']['usercontribs']:
			pageid=contribJson['pageid'] if 'pageid' in contribJson else ""
			pagetitle=contribJson['title'] if 'title' in contribJson else ""
			if pageid not in imageidlist and pagetitle not in imagetitlelist:
				imageidlist.append(pageid)
				imagetitlelist.append(pagetitle)
				print("[用贡][新图]","\t[User]",username,"\t[File]",pageid,"\t",pagetitle)
				image_new+=1
			else:
				#print("[用贡][图]","\t[User]",username,"\t[File]",pageid,"\t",pagetitle)
				pass
		uccontinue=isResponceContinue(json)
		if not uccontinue:
			break

print()
end_time=time.time()
print("ended   at",time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(end_time)))
print(second2days.main(end_time-start_time),"spent.")

print(image_new,"images found.")

input("Done.")