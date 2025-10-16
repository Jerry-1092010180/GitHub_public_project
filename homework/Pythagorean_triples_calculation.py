print('此程序的版本号Version1.0.3\n此程序的创作者是刘家瑞\n版权来自Glory工作室\n若有问题，请联系电话18839957639\nThank you!')
import time
sum = 1
timeflush = 0.25
for i in range(0, int(sum / timeflush)):
    list = ["\\", "|", "/", "-"]
    index = i % 4
    print("\r程序正在启动{}".format(list[index]), end="")
    time.sleep(timeflush)
import math
print('欢迎使用勾股计算程序！(请点击下一行，再回车)')
input()
def C(a, b):
    c = a ** 2 + b ** 2
    result = math.sqrt(c)
    return result
def A(c, b):
    a = c ** 2 - b ** 2
    result = math.sqrt(a)
    return result
def B(c, a):
    b = c ** 2 - a ** 2
    result = math.sqrt(b)
    return result
while 1:
    print('您将要输入最短边和中等边吗？(yes/no)')
    answer = input('是或否：').lower()
    '''问题所在'''
    if answer =='q':
        print('再见，使用愉快！')
        break
        ############
    if answer == 'yes' or answer == 'no':
        if answer == 'yes':
            a = int(input('最短边的长度：'))
            b = int(input('中等边的长度：'))
            while 2:
                if a > b:
                    print('这是一个数学错误，请重新输入。')
                    a = int(input('最短边的长度：'))
                    b = int(input('中等边的长度：'))
                    if a<b:
                        break
                else:
                    break
            print('斜边的长度为：')
            print(C(a, b))
            print('请问您还要继续计算吗？(yes/no)')
            answer = input('是或否：').lower()
            if answer == 'yes':
                print('好的，正在刷新中……')
                continue
            if answer == 'no':
                print('再见，使用愉快！')
                break
            if answer != 'yes' and answer != 'no':
                print('输入错误，请重试。')
                continue
        if answer == 'no':
            print('您是要输入最短边和斜边或中等边和斜边吗？第一种请输入1,第二种请输入2。')
            answer = int(input('请输入：'))
            if answer == 1:
                a = int(input('最短边的长度：'))
                c = int(input('斜边的长度：'))
                while 3:
                    if a > c:
                        print('这是一个数学错误，请重新输入。')
                        a = int(input('最短边的长度：'))
                        c = int(input('斜边的长度：'))
                        if a < c:
                            break
                    else:
                        break
                print('中等边的长度为：')
                print(B(c, a))
            if answer == 2:
                b = int(input('中等边的长度：'))
                c = int(input('斜边的长度：'))
                while 4:
                    if b > c:
                        print('这是一个数学错误，请重新输入。')
                        b = int(input('中等边的长度：'))
                        c = int(input('斜边的长度：'))
                        if b < c:
                            break
                    else:
                        break
                print('最短边的长度为：')
                print(A(c, b))
            if answer < 1 and answer > 2:
                print('输入错误，请重试。')
                continue
            print('请问您还要继续计算吗？(yes/no)')
            answer = input('是或否：').lower()
            if answer == 'yes':
                print('好的，正在刷新中……')
                continue
            if answer == 'no':
                print('再见，使用愉快！')
                break
            if answer != 'yes' and answer != 'no':
                print('输入错误，请重试。')
                continue
    else:
        print('输入错误，请重新输入。')
    continue