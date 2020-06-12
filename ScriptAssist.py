import os
import numpy as np
hdx_file=os.path.join('template.csv')
hdx=np.genfromtxt(fname=hdx_file, delimiter=',', dtype='unicode')
data=hdx[1:,1:]
num_rows=len(data[:,0])
limitArr=[]
timePts=int(len(data[0,3:])/5)
lastCol=3+timePts*2
ttestColNo=4*timePts
protLen=input("Give the length of the protein: ")
nocArr=[]
if int(data[0,1])!=1:
    nocArr.append(F'1-{int(data[0,0])-1}')
for i in range(1,num_rows):
    lastEnd=int(data[i-1,1])
    start=int(data[i,0])
    if start>lastEnd+1:
        nocArr.append(F'{lastEnd+1}-{start-1}')
if int(data[num_rows-1,1])<int(protLen):
    nocArr.append(F'{int(data[num_rows-1,1])+1}-{protLen}')
d=","
print(F'Peptides not covered in this data set: {d.join(nocArr)}')    
varType=input("Is this a protection or exposure? (Type P for protection and E for exposure): ")
while varType!='P' and varType!='E':
    varType=input("Invalid Entry. Type P or E: ")
upper=input("Enter upper-limit: ")
limitArr.append(upper)
lower=input("Enter lower-limit: ")
limitArr.append(lower)
pepArr=[]
if varType=='P':
    for i in range(num_rows):
        x=ttestColNo
        for j in range(3,lastCol,2):
            if float(data[i,j])>=int(limitArr[1]) and float(data[i,j])<int(limitArr[0]) and float(data[i,j+2*timePts])>=0.4 and float(data[i,j+x])<=0.01:
                string=F'{data[i][0]}-{data[i][1]}'
                if not string in pepArr:
                    pepArr.append(string)
            x-=1
    print(d.join(pepArr))
if varType=='E':
    l=-int(limitArr[1])
    u=-int(limitArr[0])
    for i in range(num_rows):
        x=ttestColNo
        for j in range(3,lastCol,2):
            if float(data[i,j])<=l and float(data[i,j])>u and abs(float(data[i,j+2*timePts]))>=0.4 and float(data[i,j+x])<=0.01:
                string=F'{data[i][0]}-{data[i][1]}'
                if not string in pepArr:
                    pepArr.append(string)
            x-=1
    print(d.join(pepArr))
    
    
    
