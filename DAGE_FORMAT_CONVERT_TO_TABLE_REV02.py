#!/usr/bin/env python
# coding: utf-8

# # Name: DAGE_FORMAT_CONVERT_TO_TABLE_REV02
# Author: Duong, Van Binh
# Date: 2019, May, 03
# feature:
#     + Input: "PULL_x.csv" and "SHEAR_x.csv"
#     + Output: "final_pull_shear.csv"

# In[ ]:
import os
import argparse
import csv

# In[]
parser=argparse.ArgumentParser(description="This use for convert the PULL and Share Dage Nordson Format to table format")
parser.add_argument('-p','--path',default='.')
parser.add_argument('-o','--outfile',default="final_pull_shear.csv")

args=parser.parse_args()
print(args.__dict__)


# listing pull and shear csv file
temp01=os.listdir(args.path)
temppull=[]
tempshear=[]
tempfull=[]
for i in temp01:
    if ".csv"and "PULL_" in i:
        temppull.append(i)
        tempfull.append(i)
    if ".csv" and "SHEAR_" in i:
        tempshear.append(i)
        tempfull.append(i)
    
print("list pull file: ")
print(temppull)
print("list shear file: ")
print(tempshear)
print("list full file: ")
print(tempfull)


# In[2]:


result01=[]
result01.append(["FILE_NAME","DATE","TIME","ENTITY",
                 "IPN_CARTRIDGE","TYPE_FORCE","WIRE_ID",
                 "FORCE"])
for filename in tempfull:
    print("filename: ",filename)
    #print(filename)
    f=open(filename,'r')
    temp01=f.readlines()
    #
    #print(result01)
    #
    ilist=[]
    for idx,val in enumerate(temp01):
        if "TESTER" in val:
            ilist.append(idx)
    #print(ilist)
    ##
    for ii in range(len(ilist)-1):
        idate="NA";itime="NA";ibatch="NA";icartridge02="NA"
        icartridge03="NA";itest01="NA";itest03="NA"
        ipull="NA";ishear="NA"
        for idx,val in enumerate(temp01[ilist[ii]:ilist[ii+1]]):
            if "DATE" in val: idate=val.split(',')[1].rstrip()  
            if "TIME" in val: itime=val.split(',')[1].rstrip() 
            if "BATCH" in val: ibatch=val.split(',')[1].rstrip() 
            if "CARTRIDGE" in val: 
                icartridge02=val.split(',')[2].rstrip() 
                icartridge03=val.split(',')[3].rstrip() 
            if "TEST\"" in val:       
                itest01=val.split(',')[1].rstrip() 
                itest03=val.split(',')[3].rstrip()   
        temp02=[filename,idate,itime,ibatch,icartridge02,icartridge03,itest01,itest03]
        result01.append(temp02)
    ## final TESTER 
    idate="NA";itime="NA";ibatch="NA";icartridge02="NA"
    icartridge03="NA";itest01="NA";itest03="NA"
    ipull="NA";ishear="NA"
    for idx,val in enumerate(temp01[ilist[-1]:]):
        if "DATE" in val: idate=val.split(',')[1].rstrip()  
        if "TIME" in val: itime=val.split(',')[1].rstrip() 
        if "BATCH" in val: ibatch=val.split(',')[1].rstrip() 
        if "CARTRIDGE" in val: 
            icartridge02=val.split(',')[2].rstrip() 
            icartridge03=val.split(',')[3].rstrip() 
        if "TEST\"" in val:       
            itest01=val.split(',')[1].rstrip() 
            itest03=val.split(',')[3].rstrip()  

    temp02=[filename,idate,itime,ibatch,icartridge02,icartridge03,itest01,itest03]
    result01.append(temp02)
    f.close()
    
## save to table csv file
with open(args.outfile,"w") as f:
    writer=csv.writer(f)
    writer.writerows(result01)
f.close()


# In[ ]:




