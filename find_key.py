'''

Question : WAP to find out the first key that maps to a value given by the user

'''

#PROGRAM

dct = eval(input('Enter Dictionary : '))
val = eval(input('Enter the Value to be checked : '))
print()
for i in dct:
    if dct[i] == val:
           key = i
           break
print('Key = ',key)
        
