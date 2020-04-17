'''

Use of fromkeys() method.
WAP to create a List of Names of students . Create Another list which contains the length of the strings (names of students) entered in the first List .
With the help of these Lists create a Dictionary in which names will be acting as keys and length of strings will be acting as values.

'''

#PROGRAM

dct = dict()
ls1 = eval(input('Enter names of Students : '))
ls2 = [len(i) for i in ls1]
dct = dct.fromkeys(ls1)
j = 0
for i in dct:
    dct[i] = ls2[j]
    j += 1
print()    
print('Resultant Dictionary :',dct)    
