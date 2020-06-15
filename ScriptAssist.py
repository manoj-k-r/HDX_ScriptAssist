import csv
with open('template.csv') as input, open('template01.csv','wb') as output:
	writer=csv.writer(output)
	for row in csv.reader(input):
		if any(field.strip() for field in row):
			writer.writerow(row)
import os
import numpy as np
hdx_file=os.path.join('template01.csv')
hdx=np.genfromtxt(fname=hdx_file, delimiter=',', dtype='unicode')
data=hdx[1:,1:]
num_rows=len(data[:,0])
limitArr=[]
timePts=int(len(data[0,3:])/5)
lastCol=3+timePts*2
ttestColNo=4*timePts
decision=raw_input("Do you want peptides not covered in this dataset? Type Y or N: ")
while decision!="Y" and decision!="N":
    decision=raw_input("Invalid entry. Type Y or N")
if decision=='Y':
    protLen=raw_input("Give the length of the protein: ")
    nocArr=[]
    if int(data[0,1])!=1:
        nocArr.append("1-"+str(int(data[0,0])-1))
    for i in range(1,num_rows):
        ends=data[:i,1]
        maxEnd=max(ends.astype(int))
        start=int(data[i,0])
        if start>maxEnd+1:
            nocArr.append(str(maxEnd+1)+"-"+str(start-1))
    if int(data[num_rows-1,1])<int(protLen):
        nocArr.append(str(int(data[num_rows-1,1])+1) + "-" + protLen)
    d=","
    print("Peptides not covered in this data set:" + (d.join(nocArr)))    
varType=raw_input("Is this a protection or exposure? (Type P for protection and E for exposure): ")
while varType!='P' and varType!='E':
    varType=raw_input("Invalid Entry. Type P or E: ")
upper=raw_input("Enter upper-limit: ")
limitArr.append(upper)
lower=raw_input("Enter lower-limit: ")
limitArr.append(lower)
pepArr=[]
d=","
if varType=="P":
    for i in range(num_rows):
        x=ttestColNo
        for j in range(3,lastCol,2):
            if float(data[i,j])>=int(limitArr[1]) and float(data[i,j])<int(limitArr[0]) and float(data[i,j+2*timePts])>=0.4 and float(data[i,j+x])<=0.01:
                string=(data[i][0])+"-"+(data[i][1])
                if not string in pepArr:
                    pepArr.append(string)
            x-=1
    print(d.join(pepArr))
if varType=="E":
    l=-int(limitArr[1])
    u=-int(limitArr[0])
    for i in range(num_rows):
        x=ttestColNo
        for j in range(3,lastCol,2):
            if float(data[i,j])<=l and float(data[i,j])>u and abs(float(data[i,j+2*timePts]))>=0.4 and float(data[i,j+x])<=0.01:
                string=(data[i][0])+"-"+(data[i][1])
                if not string in pepArr:
                    pepArr.append(string)
            x-=1
    print(d.join(pepArr))
    
    
    
