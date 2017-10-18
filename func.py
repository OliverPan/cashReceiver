# -*- coding: UTF-8 -*-
from Product import *

def initDict(dict):
    fi = open("product.txt", "r")
    for line in fi.readlines():
        lis = line.split(' ')
        lis[2] = lis[2][:-1]
        dict[lis[0]] = (lis[1], lis[2])
    fi.close()

def addProduct(prod, dict):
    '''用字典来存储商品'''
    dict[prod.number] = (prod.name, prod.price)


def delProduct(prod, dict):
    '''将商品从字典中删除'''
    del dict[prod.number]


def CashIn(dict):
    sum = 0
    '''打印小票'''
    fi = open("ticket.txt", "w+")
    fi.truncate()
    while True:
        INPUT = raw_input("请输入商品编号和数量，用空格隔开：")
        if not INPUT:
            fi.write("总价格："+str(sum))
            fi.close()
            return sum
        lis = INPUT.split(' ')
        print lis
        number = lis[0]
        shuliang = int(lis[1])
        sum += float(dict[number][1]) * shuliang
        fi.write("商品名称：" + dict[number][0] + ' ' + "商品编号:" + number + ' ' + "商品价格：" + dict[number][1] + ' ' + "商品数量：" + lis[1])
    return sum

def reload(dict):
    fi = open("product.txt", "w+")
    fi.truncate()
    for key in dict.keys():
        fi.write(key + ' ' + dict[key][0] + ' ' + dict[key][1] +'\n')
    fi.close()


if __name__ == "__main__":
    dict = {}
    try:
        fi = open("product.txt", "r+")
        fi.close()
    except(IOError):
        fi = open("product.txt", "w+")
        fi.close()
    initDict(dict)
    print "欢迎使用银行收银系统"
    print "1. 添加新的商品如库"
    print "2. 从库中删除已有商品"
    print "3. 查看库中所有商品"
    print "4. 收银并打印小票"
    print "5. 结束并关闭系统"
    print "请输入对应序号实现功能："

    while True:
        switch = input()
        if switch in range(1, 6):
            break
        else:
            print "输入不符合规则，请重新输入："
    while not switch == 5:
        if switch == 1:
            name = raw_input("请输入商品名称：")
            number = raw_input("请输入商品编号：")
            price = raw_input("请输入商品价格：")
            product = Product(number, name, price)
            addProduct(product, dict)
            print "成功!"
            switch = input("请输入对应序号实现功能：")
        elif switch == 2:
            number = raw_input("请输入要删除商品编号：")
            product = Product(number, dict[number][0], dict[number][1])
            delProduct(product, dict)
            switch = input("请输入对应序号实现功能：")
        elif switch == 3:
            for key in dict.keys():
                print (key, dict[key][0], dict[key][1])
            switch = input("请输入对应序号实现功能：")
        else:
            sum = CashIn(dict)
            print "小票已经打印，总价格为："+str(sum)
            switch = input("请输入对应序号实现功能：")
    if switch == 5:
        reload(dict)
