#!/usr/bin/env  python
# encoding=UTF-8
loop=True
money=0
while loop:
    x = raw_input('提示：请投入金币,结束投币请按"q"键:')
    if x=='q':
        if money==0:
            print '错误：您未投入过纸币，请至少投入一张纸币后才能选购商品'
        else:
            print '提示：您已结束投币，将进入购买商品操作界面'
            loop = False
    else:
        try:
            x = int(x)
            money+=x
            print '提示：您此次投币',x,'元人民币，您一共投币',money,'元人民币'
        except Exception,e:
            print '错误：您的金币系统不识别，请重新投币，谢谢！'
 
GoodList = {
    '可口可乐':2.5,
    '果粒橙':3,
    '奶茶':1.5,
    '加多宝':4
}
 
i=0
print '请选择商品：'
for x in GoodList:
    i+=1
    print '编号',i,'商品名称',x,'价格',GoodList[x]
print
 
fanwei = range(len(GoodList))
loop = True
while loop:
    o = raw_input('提示：请输入您要购买的商品编号，按"q"键结束购买')
    if o=='q':
        loop = False
    else:
        try:
            o = int(o)
            if o>=1 and o<=len(GoodList):
                i=0
                for x in GoodList:
                    i+=1
                    if i==o:
                        if money>=GoodList[x]:
                            money -= GoodList[x]
                            print '提示：您购买的商品是:',x,'，价格:',GoodList[x],'，您还剩余：',money,'元人民币'
                            if money==0:
                                loop = False
                        else:
                            print '错误：您的余额',money,'元已不足购买此商品',x,'[',GoodList[x],'元]'
            else:
                print '错误：您输入的商品编号不存在，请重新输入'
        except Exception,e:
            print '错误：请输入正确的产品编号，谢谢合作！'
 
if money>0:       
    print '提示：系统将找您，',money,'元人民币，欢迎下次光临!!'
else:
    print '提示：您的余额已用完，欢迎下次光临!!'
