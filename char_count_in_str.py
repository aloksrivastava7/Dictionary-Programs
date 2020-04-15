'''

Question - WAP to calculate the number of times a particular character is present in the given string (USING DICTIONARY)


'''

#PROGRAM

dct = dict()
s = input('Enter String : ')
print()
for i in s:
    if i not in dct:
        dct[i] = 1
    else :
        dct[i] += 1
print('Character\t \tFrequency')
print()
for i in dct:
    print(i,'\t\t:\t',dct[i])
    
    
