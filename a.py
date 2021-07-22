import re
import pandas as pd
import os
import tkinter.filedialog
import datetime


fTyp = [("txt file", ".txt")]
iDir = os.path.abspath(os.path.dirname(__file__))
file_name = tkinter.filedialog.askopenfilename(filetypes=fTyp, initialdir=iDir)

file = open(file_name,"r")
moziretu = file.read()
file.close()
#moziretu="[05:17:05] bouninng > <url=showinfo:47975//1036779110498>Crystalline Isogen-10*</url>  <url=showinfo:48112//1036778188809>Zero-Point Condensate*</url>"
r = re.findall("showinfo:\d+", moziretu)
#print(r)
#":\d+//"
u = moziretu.replace("*","")
t = re.findall(">\w.+?</url>",u)

#print(u)
#w = v[2:-1] for v in u
id = []
name = []
for i in range(len(r)):
    J = r[i]
    K = t[i]
#    print(J[1:-2])
#    print(K[2:-1])
    j = J[9:]
    k = K[1:-6]
    id.append(j)
    name.append(k)

#print(id)
#print(name)
l2d = []
l2d.append(name)
l2d.append(id)
df1 = pd.DataFrame()
df1["name"] = name
df1["id"] = id
#df1.to_csv('./df1.csv', header=False, index=False)

dt_now = datetime.datetime.now()
daydate=str(dt_now.strftime("%m%d_%H%M%S"))
df1.to_csv("./"+daydate+".csv", header=False, index=False)
