theList = []
theList.append(1)
theList.append(2)
theList.append(3)
print(theList[0]) #prints 1
print(theList[1]) #prints 2

for x in theList:
    print(x)
    #prints 1,2,3

#other methods (to ignore for beginners) :
#method 1
print (str(theList[0]) + " " +str(theList[1])+ " " + str(theList[2]))
#method 2
for x in theList:
    print(x, end=",")
#method 3
x=" "
for y in theList:
    x = x + str(y)+ ","
    #x+= str(y)+ ","
print(x)

