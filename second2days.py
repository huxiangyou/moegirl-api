"""
Convert a second-time to a year-day-hour-minute-second time
Python 3.7.4
Hu Xiangyou Oct 3, 2019
"""

def f(num:float,unit:str)->str:
	if num>1:
		return str(num)+" "+unit+"s"
	if num>0:
		return str(num)+" "+unit
	if num==0:
		return ""
	else:
		return "ERROR"

def main(seconds:float=0.00)->str:
	m,s=divmod(seconds,60)
	h,m=divmod(m,60)
	d,h=divmod(h,24)
	y,d=divmod(d,365)

	y=int(y)
	d=int(d)
	h=int(h)
	m=int(m)
	s=round(s,2)

	return " ".join(i for i in (f(y,"year"),f(d,"day"),f(h,"hour"),f(m,"minute"),f(s,"second")) if i)
