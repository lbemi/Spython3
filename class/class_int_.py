class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart
        print(self)  #self 代表的是类的实例，代表当前对象的地址
        print(self.__class__) #self.class 指向类

x = Complex(3.0, -4.5)
print(x.r, x.i)