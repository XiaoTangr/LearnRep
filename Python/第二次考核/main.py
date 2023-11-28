#coding:utf-8
# G22计算机应用技术7班 唐志平@2023年11月14日

# printf实现c语言方法
def printf(format_str, *args):
    if len(args) == 0:
        print(format_str)
    else:
        print(format_str % args)


#=================================第一题=======================================
class Q1(object):

   def __init__(self):
       pass

   def list_cfg(self):
       # 创建一个列表
       Texts = ['Tang', 'Zhi', 'Ping']
       # list方法
       Texts1 = list("abcd")


       print("初始列表:")
       print("\tTexts:", Texts)
       print("\tTexts1:", Texts1)

       # append追加元素
       Texts.append('Love')
       print("追加元素后的列表:")
       print("\tTexts:", Texts)

       # 在指定索引处插入元素
       Texts.insert(1, 'InsertText')
       print("由索引添加元素后的列表:")
       print("\tTexts:", Texts)

       # 删除指定索引处的元素
       Texts.pop(2)
       print("指定索引删除后的列表:")
       print("\tTexts:", Texts)

       # remove方法匹配值删除
       Texts.remove('InsertText')
       print("指定值删除后的列表:")
       print("\tTexts:", Texts)

       # del方法匹配索引删除
       del Texts1[1]
       print('del方法匹配索引删除元素后的列表:')
       print('\tTexts1:', Texts1)


       # 替换指定索引处的元素
       Texts[2] = 'ChangeText'
       print("由索引替换元素后的列表:")
       print("\tTexts:", Texts)


   def combine_cfg(self):
       # 创建一个元组
       Texts = ('Tang', 'Zhi', 'Ping')

       # 尝试修改元组元素将引发错误
       # Texts[1] = 'ChangeText'  
       # 这将会报错：cannot modify an immutable list

       # 创建一个新的元组
       new_Texts = ('Love', 'You')

       print("创建的两个元组:")
       print("\tTexts:", Texts)
       print("\tnew_Texts:", new_Texts)
       # 连接两个元组
       combined_Texts = Texts + new_Texts
       print("连接后的元组:")
       print("\tcombined_Texts:", combined_Texts)
       # 这将输出 ('Tang', 'Zhi', 'Ping', 'Love', 'You')

       # 重复元组
       repeated_Texts = Texts * 3
       print("重复后的元组:")
       print("\trepeated_Texts:", repeated_Texts)
       # ('Tang', 'Zhi', 'Ping', 'Tang', 'Zhi', 'Ping', 'Love', 'You')



   def dict_cfg(self):
       # 创建一个字典
       person = {'name': 'John', 'age': 30, 'city': 'New York'}
       print("创建一个字典:")
       print("\tperson:", person)
       # 添加键值对
       person['job'] = 'developer'
       print("添加键值对后的字典:")
       print("\tperson:", person)
       # 输出：{'name': 'John', 'age': 30, 'city': 'New York', 'job': 'developer'}

       # 删除键值对
       del person['job']
       print("删除键值对后的字典:")
       print("\tperson:", person)
       # 输出：{'name': 'John', 'age': 30, 'city': 'New York'}

       # 更新键值对
       person['age'] = 31
       print("更新键值对后的字典:")
       print("\tperson:", person)
       # 输出：{'name': 'John', 'age': 31, 'city': 'New York'}

   def Test(self):
       print("列表:")
       self.list_cfg()
       print('\n元组:')
       self.combine_cfg()
       print('\n字典:')
       self.dict_cfg()



#=================================第一题=======================================
class Fruit():
    name = "水果"
    color = "未知"
    # 构造方法
    def __init__(self, name, color):
        self.color = color
        self.name = name
    
    # 定义抽象方法
    def cut(self):
        pass

    # 定义成员方法
    def GetInfo(self):
        printf("这个水果的名字是%s,颜色是%s", self.name, self.color)

class Plant():
    name = "植物"
    type = "未知"

    def __init__(self, name, type):
        self.type = type
        self.name = name

    def GetInfo(self):
        printf("这个植物的名字是%s,类型是%s", self.name, self.type)

# 单一继承
class Orange(Fruit):
    pices = 0

    def __init__(self, name, color,pices):
        super().__init__(name, color)
        self.pices = pices

    # 实现抽象方法
    def cut(self):
        printf("橘子被剥开了")
    # 覆写方法
    def GetInfo(self):
        printf("这个橘子的名字是%s,颜色是%s", self.name, self.color)

# 多继承
class Apple(Fruit,Plant):
    def __init__(self, name, color,type):
        super().__init__(name, color)
        self.type = type

    def GetInfo(self):
        # 父类方法调用
        Plant.GetInfo(self)
        Fruit.GetInfo(self)


#=================================测试内容=======================================
def main():

    printf("-------问题1--------")
    question1 = Q1()
    question1.Test()


    printf("\n\n\n\n-------问题2--------")
    # 实例化对象
    orange1 = Orange("好吃的橘子", "橘红色", 10)
    apple1 = Apple("红富士", "红色", "苹果树")

    printf("Orange类：")
    printf("获取信息方法：")
    orange1.GetInfo()
    printf("切水果方法：")
    orange1.cut()
    

    printf("\nApple类：")
    printf("获取信息方法：")
    apple1.GetInfo()
    printf("切水果方法,抽象方法未实现，无输出")
    apple1.cut()    

if __name__ == "__main__":
    main()