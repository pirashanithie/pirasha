##find the given word palindome or not and find longest palindrome

inpu=list(input())
inword=list(inpu)
k=0
li=[]
for i in range(0,len(inword)):
    coun=inword.count(inword[i])
    if coun>=2:
        intu=tuple(inword)
        inta=list(intu)
        for j in range(0,coun-1):
            inta.remove(inword[i])


        ind=inta.index(inword[i])
        ind=ind+coun
        
        re=inpu[i:ind]
        if re==re[::-1]:
            li.append(re)

if len(li)>0:
    mali=max(li)
    st=''
    if len(mali)>1:
        for i in range(0,len(mali)):
            st+=mali[i]

        print(st)

else:
    print('asdf')

    
