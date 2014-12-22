print ">>>>>>>>>>>>>>>>>>>list"
classmates = ['Michael','Bob','Tracy']
print classmates
print len(classmates)
print classmates[0]
print classmates[1]
print classmates[2]
print classmates[-1]
print classmates[-2]
print classmates[-3]
classmates.append('Adam')
print classmates[-1]
classmates.insert(1,'Jack')
print classmates[1]
classmates.pop()
print classmates[-1]
classmates[1] = 'Sarah'
print classmates[1]
classmates[-1] = 123
print classmates
classmates.append(['python', 'java', 'php']);
print classmates
print classmates[-1]
print classmates[-1][1]
print ">>>>>>>>>>>>>>>>>>>tuple"
classmates = ('Michael', 'Bob', 'Tracy')
print classmates
t = (1, 2)
print t
t= ()
print t
t = (1)
print t
t = (1,)
print t
print t[-1]
modifyT = ('a', 'b', ['A', 'B'])
print modifyT
modifyT[-1].append('C')
print modifyT
modifyT[-1][-2] = 'Y'
print modifyT