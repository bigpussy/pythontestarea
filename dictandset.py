# -*- coding: utf-8 -*-
print u"dict 演示"
d = {'Micheal':95, 'Bob':75, 'Tracy':85}
print d['Micheal']
d['Tom'] = 80
print d['Tom']
print u"set 演示"
s = set([1, 2, 3])
print s
s.add(4)
print s
s.add(4)
print s
s.remove(4)
print s
print u"set可以看成数学意义上的无序和无重复元素集合"
print u"因此，两个set可以做数学意义上的交集"
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print s1 & s2
print s1 | s2

