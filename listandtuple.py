# -*- coding: utf-8 -*-
print ">>>>>>>>>>>>>>>>>>>list"
print u"创建一个list"
classmates = ['Michael','Bob','Tracy']
print classmates
print u"可以获取长度"
print len(classmates)
print u"每个元素可以用相应id索引出来"
print classmates[0]
print classmates[1]
print classmates[2]
print u"也可以倒着获取出来"
print classmates[-1]
print classmates[-2]
print classmates[-3]
print u"可以在后面添加元素"
classmates.append('Adam')
print classmates[-1]
print classmates
print u"也可以插入到某个位置"
classmates.insert(1,'Jack')
print classmates
print classmates[1]
print u"弹出最后一个元素，删除"
classmates.pop()
print classmates[-1]
print u"也可以修改某个位置的元素"
classmates[1] = 'Sarah'
print classmates[1]
print u"list还可以加入不同类型的数据"
classmates[-1] = 123
print classmates
print u"可以包含另外一个list"
classmates.append(['python', 'java', 'php']);
print classmates
print classmates[-1]
print classmates[-1][1]
print ">>>>>>>>>>>>>>>>>>>tuple"
print u"新建一个tuple"
classmates = ('Michael', 'Bob', 'Tracy')
print classmates
print u"这样新建没问题"
t = (1, 2)
print t
print u"一个空的"
t= ()
print t
print u"这样就当做一个数了，因为和括号操作冲突，python按照括号来算"
t = (1)
print t
print u"所以要建立只有一个元素的，这样做"
t = (1,)
print t
print t[-1]
print u"这样就建立一个可以修改的tuple了"
modifyT = ('a', 'b', ['A', 'B'])
print modifyT
print u"因为指向了一个可以改变的list"
modifyT[-1].append('C')
print modifyT
modifyT[-1][-2] = 'Y'
print modifyT
