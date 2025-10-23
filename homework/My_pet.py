import time
class User:
    def __init__(self, name):
        self.name = name
        self.live = 100
        self.lastMeal = time.time()
        self.bornTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    def all_answer(self):
        now = time.time()
        time_diff = now - self.lastMeal
        current_life = max(0, self.live - int(time_diff))
        print(f'\n距离上次喂食已过去{int(time_diff)}秒')
        print(f'生命值：{current_life}')
        return current_life
    def feed(self):
        self.live = 100
        self.lastMeal = time.time()
        print(f'谢谢，{self.name}吃饱了！')
    def first(self):
        print(f'我叫：{self.name}')
    def second(self):
        self.feed()
    def third(self):
        print(f'我的生日是：{self.bornTime}')
    def forth(self):
        print(f'主人和我说话了！{self.name}好开心！')
    def fifth(self):
        print(f'讨厌，人家还小！')
    def sixth(self):
        print('叮叮当，叮叮当，铃儿响叮当')
    def check(self):
        now = time.time()
        time_diff = now - self.lastMeal
        current_life = max(0, self.live - int(time_diff))
        if current_life <= 0:
            print(f'\n对不起，由于长时间没有喂食，您的宠物{self.name}已经饿死了…')
            return False
        return True
    def out(self, action):
        action_num = int(action)
        if action_num == 1:
            self.first()
        elif action_num == 2:
            self.second()
        elif action_num == 3:
            self.third()
        elif action_num == 4:
            self.forth()
        elif action_num == 5:
            self.fifth()
        elif action_num == 6:
            self.sixth()
        else:
            print('请输入1～6之间的数字')
            return
        self.all_answer()
agree = input("请给你的宠物起个名字:")
a = User(agree)
while a.check():
    print('-------------------')
    user_input = input("主人您好，您想对我干什么？\n"
                      "1.问名字 2.喂食 3.问生日\n"
                      "4.打招呼 5.说'我爱你' 6.让我唱歌: ")
    try:
        a.out(user_input)
    except ValueError:
        print('输入错误类型，请重新输入')