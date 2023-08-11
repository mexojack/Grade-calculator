#Devoir de Jacky Mexilas

kantite= input ("Antre kantite not wap bezwen antre yo: \n")
lis_not=[]
kantite= int(kantite)
a=1
p=1

while (a<=kantite):
    not_yo= input ("Antre not nimero an")
    lis_not.append(int(not_yo))
    a+=1

total=0
for el in lis_not:
    total=total+ el

mwayenn=total/kantite

if (mwayenn>=90):
    print("Mwayenn nan se: ",mwayenn,"klasifikasyon an se: A")

elif (mwayenn>=80 and mwayenn<90):
    print("Mwayenn nan se: ",mwayenn,"klasifikasyon an se: B")
    
elif (mwayenn >=70 and mwayenn<80):
    print ("Mwayenn nan se: ",mwayenn,"klasifikasyon an se: C")
    
elif (mwayenn >=60 and mwayenn<70):
    print ("Mwayenn nan se: ",mwayenn,"klasifikasyon an se: D")
    
else:
    print("Mwayenn nan se: ",mwayenn,"klasifikasyon an se: F")
