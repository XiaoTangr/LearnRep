# 面对对象程序设计的三大特征：封装，继承，多态。
# 类的定义
'''类是一种抽象的概念，用来描述具有相同属性和行为的对象的集合，
是封装对象属性和行为的载体，定义了该集合中每个对象所共有的属性和行为。
对象是类的实例，通过类可以创建多个对象。
从类到生成对象的过程称为类的实例化。'''


# 类的定义用class关键字来实现.   pass占位符
# 类的实例化（用类创建一个对象）
class Person:
    pass


# 对象绑定属性和功能
'''对象是一个抽象的概念，可以表示任意事物，对象分为静态（属性）和动态（行为或者方法）两部分，
通过类定义的数据结构实例，对象包括两个数据成员（类变量和实例变量）和方法，类是对象的抽象，对象是类的具体化(实例)。
一个完整的对象具有属性和行为（或方法）。'''

# 类的继承
'''继承是实现重复利用的重要手段，子类通过继承复用了父类（基类）的属性和行为的同时，又添加了子类（派生类）特有的属性和行为。
即一个派生类继承基类的字段和方法，继承也允许把一个派生类的对象作为一个基类对象对待。继承分为单继承和多继承'''


# 单继承
class 人类:  # 类定义
    姓名 = ''  # 定义2个基本属性
    年龄 = ''
    __体重 = 0  # __定义私有属性，私有属性在类外部无法直接访问

    def __init__(self, xm, nl, tz):  # 定义构造方法
        self.姓名 = xm
        self.年龄 = nl
        self.__体重 = tz

    def speak(self):
        print("%s说:我%d岁了" % (self.姓名, self.年龄))


class 学生(人类):
    年级 = ''  # 定义属于子类的属性

    def __init__(self, xm, nl, tz, nj):
        人类.__init__(self, xm, nl, tz)  # 调用父类的构造方法
        self.年级 = nj

    def speak(self):  # 复写父类的方法
        print("\n%s说:我%d岁了,我在读%d年级" % (self.姓名, self.年龄, self.年级))





# 多继承
class 兼职():
    工资 = ''

    def __init__(self, gz):
        self.工资 = gz

    def show(self):
        print("我的工资是%d/月" % (self.工资))


class 学生兼职(学生, 兼职):  # 继承了前2个类
    职业 = ''

    def __init__(self, xm, nl, tz, nj, gz, zy):
        学生.__init__(self, xm, nl, tz, nj)  # 调用学生类的构造方法
        兼职.__init__(self, gz)  # 调用兼职类的构造方法
        self.职业 = zy

    def show(self):
        print("我是%s,我的工资是%d/月" % (self.职业, self.工资))



# 方法的多态性（方法重写）
'''将父类对象应用于子类的特征就是多态，子类继承父类特征的同时，还具备了自己的特征，并且能起到不同的作用，这就是多态化的结构。
方法是类中定义的函数，如果父类继承的方法不能满足子类的需求，可以对其进行改写，这个过程叫方法的覆盖，也称为方法的重写。'''


class Fruit:  # 定义一个水果类（父类）
    color = "绿色"

    def harvest(self, color):
        print("颜色是：" + color + "的")
        print("水果被摘下来...")
        print("原来颜色是：" + Fruit.color + "的")


class Apple(Fruit):  # 定义一个苹果类（子类）
    color = "红色"

    def __init__(self):
        print("\n我是苹果")


class Orange(Fruit):  # 定义一个橘子类（子类）
    color = "橙色"

    def __init__(self):
        print("\n我是橘子")  # \n换行

    def harvest(self, color):  # 重写harvest()方法的代码
        print("橘子的颜色是：" + color + "的")
        print("橘子被摘下来之前...")
        print("橘子原来颜色是：" + Fruit.color + "的");



if __name__ == '__main__':
    学生1 = 学生("张三", 18, 60, 2)  # 创建子类实例
    学生1.speak()  # 子类的实例调用speak()方法

    学生兼职1 = 学生兼职("李四", 20, 60, 3, 700, "快递员")
    学生兼职1.speak()
    学生兼职1.show()

    apple = Apple()  # 实例化苹果类
    apple.harvest(apple.color)  # 调用父类的harvest()方法
    orange = Orange()  # 实例化橘子类
    orange.harvest(orange.color)  # 调用父类的harvest()方法
