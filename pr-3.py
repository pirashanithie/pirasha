##find given two strings anagrams


first_str=str(input('Enetr string one:')).split()
sec_str=str(input('Enter string two:')).split()
lifirst=[]
lisec=[]
for i in first_str:
    for j in i:
        lifirst.append(j.lower())
for i in sec_str:
    for j in i:
        lisec.append(j.lower())
k=0
if len(lifirst)==len(lisec):
    for i in lifirst:
        if i not in lisec:
            k=1
    if k==1:
        print('These are not anagrams')
    else:
        print('These are  anagrams')
