## find most and second most frequency numbers

in_num=input().split()
if in_num[-1]=='-1':
    
    in_num=in_num[:-2]
    if len(in_num)<=50:
        li=[]
        mo_freq=0
        s_mo_freq=0
        
        for i in (in_num):
            try:
                a=int(i)
                if i not in li:
                    x=in_num.count(i)
                    li.append(i)
                    if x>mo_freq:
                        limo=' '+str(i)
                        s_mo_freq=mo_freq
                        semo=''
                        mo_freq=x
                    elif x==mo_freq:
                        limo=limo+' '+str(i)
                    elif x>s_mo_freq:
                        s_mo_freq=x
                        semo+=' '+str(i)
                    elif x==s_mo_freq:
                        semo+=semo+' '+str(i)
                    
            except():
                print('invalid input')
        print(limo)
        print(semo)
        
                
    else:
        print('list of input not in range')
else:
    print('invalid input')
