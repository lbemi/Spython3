class people:
    name = ''
    age = ''
    __weight = ''
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print('%s 说：我今年 %d 岁了，%d斤'%(self.name, self.age, self.__weight))
class Student(people):
    grade = ''
    def __init__(self, n, a, w, g):
        people.__init__(self, n, a, w)
        self.grade = g
    def speak(self):
        print('%s 说：我今年 %d 岁了，%d年级了。'%(self.name, self.age, self.grade))

class Speak:
    topic = ''
    name = ''
    def __init__(self, n, t):
        self.topic = t
        self.name = n
    def speak(self):
        print("我叫 %s，我是一个演说家，我演讲的主题是 %s"%(self.name,self.topic))

class Sample(Speak, Student):
    a= ''
    def __init__(self, n ,a ,w ,g ,t):
        Student.__init__(self, n, a, w, g)
        Speak.__init__(self, n, t)

    #私有类定义
    def __foo(self):  # 私有方法
        print('这是私有方法')

s = people('Alen',10 ,50)
s.speak()

z = Student('Jan', 12 , 60, 5)
z.speak()

q = Sample('Ben', 12, 60, 3, 'Python')
q.speak() #调用Sample类中父类Speak的speak（）方法；即Sample类（）中第一个父类的speak（）方法；
