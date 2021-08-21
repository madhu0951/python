import re
Nameage="""
Janice is 22 and Theon is 33
Gabriel is 44 and Joey is 21

"""

ages=re.findall(r'\d{1,3}',Nameage)
names=re.findall(r'[A-Z][a-z]*',Nameage)

ageDict={}
x=0
for eachname in names:
    ageDict[eachname]=ages[x]
    x+=1
print(ageDict)
print(names)
print(ages)





if re.search("inform","we need to inform him with the latest information"):
    print("There is inform")

allinform=re.findall("inform","we need to inform him with the lateest information")
for i in allinform:
    print(i)





