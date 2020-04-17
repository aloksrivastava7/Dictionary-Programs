'''

SAMPLE INPUT : d1 = {'Teacher':'Shikshak','Book':'Pustak','Friend':'Mitr'}
               d2 = {'Shikshak':'Adhyapak','Pustak':'Kitab','Mitr':'Dost'}
               
SAMPLE OUTPUT : Teacher in Hindi means Shikshak and in Urdu means Adhyapak
                Book in Hindi means Pustak and in Urdu means Kitab
                Friend in Hindi means Mitr and in Urdu means Dost

'''

#PROGRAM

d1 = eval(input('Enter First Dictionary : '))
d2 = eval(input('Enter Second Dictionary : '))
print()
for i in d1:
    print(i,'in Hindi means',d1[i],'and in Urdu means',d2[d1[i]])
