def mysplit(str,ch):
    x,y,z=str.split(ch)
    return int(x),int(y),int(z)

str="2018-07-10T10:27:48"
date,time=str.split('T')
yr,mon,day=mysplit(date,'-')
hr,min,sec=mysplit(time,':')
print("date:",yr,"-",mon,"-",day)
print("time:",hr,":",min,":",sec)