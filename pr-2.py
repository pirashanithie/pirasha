#find the number abundant or defeceency or perfect

try:
    num=int(input())
    li=[]
    sum_di=0
    if 0<=num<=10000:
        for i in range(1,num+1):
            if num%i==0:
                sum_di+=i
        if sum_di>(2*num):
            x=sum_di-(2*num)
            print(num,'is abundant by',x)
            
        elif sum_di==(2*num):
            print(num,'is perfect')
            
        else:
            x=(2*num)-sum_di
            print(num,'is deficient by',x)
except:
    print('invalid input')
    
