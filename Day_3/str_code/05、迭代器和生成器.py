# coding:utf-8
'''
@author: 猫大白
Project:Python的迭代器和生成器
'''

# 迭代器
class A:
    start = 1
    def __iter__(self):
        return self

    def __next__(self):
        if self.start>10:
            raise  StopIteration
        self.start += 2
        return self.start



# 生成器
def gen():
    start = 0
    while start < 10:
        start += 2
        yield start

for i in gen():
    print(i)

# 生成器的便捷式写法
gen2 = (i for i in range(10) if i%2==0)


# 生成器和推导式不同，其中的循环不是立即执行的，只用你遍历这个生成器时才会执行
for i in gen2:
    print(i)

