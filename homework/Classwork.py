'''performance'''
'''first classwork'''
for i in range(1,10):
     a=0
     for j in range(1,10):
         a+=1
         if j<=i:
             print(f'{i}*{j}={i*j}',end=' ')
             if a==i:
                 print('')

'''second classwork'''
a=int(input('在意空调：'))
b=int(input('在意女生：'))
if a==1:
    if b==1:
        print('复旦')
    else:
        print('清华')
else:
    if b==1:
        print('北大')
    else:
        print('上交大')


'''third classwork'''
out_money = [136, 25, 27, 36, 33, 2]
in_money = [136, 25, 36, 33, 2]
a=0
difference=[]
for i in out_money:
    a+=1
    if i in in_money:
        pass
    else:
        difference.append(i)
        print(f'在第{a}项存在{i}元的差别')
print(f'综上，共存在{sum(difference)}元的财政赤字')
