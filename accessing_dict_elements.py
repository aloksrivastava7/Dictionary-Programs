'''

WAP to create a Dictionary of keys x,y and z where each key has a value as list from 11-20 , 21-30 , 31-40 respectively.\
Access the Fifth Value of Each key from the Dictionary

'''

#PROGRAM

ls = ['x','y','z']
dct = {}
dct = dct.fromkeys(ls)
j = 11
for i in dct:
    templist = []
    k = 0
    while k<10:
        templist.append(j)
        j = j + 1
        k = k + 1
    dct[i] = templist
print(dct)
for i in dct:
    lst = dct[i]
    print(lst[4])


    
