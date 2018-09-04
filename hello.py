from bean.Student import Student
name = '于东亚'
age = 17
sex = '未知'



def getBoy(strings):
    print(strings)


#getBoy(name+str(age)+sex)


def addBoy(name,age,sex):
    boy = name +str(age)+sex
    return boy

#print(addBoy(name,age,sex))

#再也new不了对象了
boy =Student(name,age,sex)
boy.print_student()
"""
#条件语句
if boy.age<18:
    print('未成年小伙计')
else:
    print('py太爽了')
#循环

count =0
while (count<10):
    print(count)
    count += 1
#for循环 names必需为 iterable
names = ['老虎','狗峰','傻逼阿福']
for name in names:
    print(name)
    """
names = ['老虎','狗峰','傻逼阿福']
'''for postion in range(0,10):
    print(postion)
    '''
#切片 取数组0- 2 ,到2结束, 不包含2
print(names[0:2])
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}

for k in d:
    print(k+" :"+str(d[k]))

l =[x+x for x in range(0,10) if x<4]
print(l)

