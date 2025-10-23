import os
base_path=os.path.dirname(__file__)
file_path=os.path.join(base_path,'report.txt')
with open(file_path,'r',encoding='utf-8')as txt:
    lines=txt.readlines()
student={}
all_name=[]
for i in lines:
    part=i.split()
    name=part[0]
    chinese=part[1]
    math=part[2]
    english=part[3]
    if name not in all_name:
        all_name.append(name)
    else:
        name=name+'2'
        all_name.append(name)
    the_sum=int(chinese)+int(math)+int(english)
    the_student={'姓名':name,
                 '语文':chinese,
                 '数学':math,
                 '英语':english,
                 '总分':the_sum}
    student[name]=the_student
sort_students=sorted(student.items(),key=lambda x:x[1]['总分'],reverse=True)
for rank, (name, getin) in enumerate(sort_students, 1):
    print(f"第{rank}名: {name}, 总分: {getin['总分']}")
question=input('请输入您想查询的学生姓名：')
if question in student:
    print(f"{question}的信息: {student[question]}")
else:
    print(f"没有找到名为 {question} 的学生")