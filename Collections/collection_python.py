from collections import namedtuple


#1.namedtuple
a=namedtuple('courses','name,technology')
s=a('data science','python')
print(s)


#2.deque
from collections import deque
a=['e','d','u','r','e','k','a']
d=deque(a)
print(d)
d.append('python')
print(d)
d.appendleft('AI')
print(d)
d.pop()
print(d)
d.popleft()
print(d)

#3.Chainmap
from collections import ChainMap
a={1:'edureka',2:'python'}
b={3:'ML',4:'AI'}
a1=ChainMap(a,b)
print(a1)



#4.Counter
from collections import Counter
a=[1,2,4,2,2,3,2,1,4,3,4,2,3,3,1]
c=Counter(a)
print(c)
print(list(c.elements()))
print(c.most_common())
sub={2:1,4:1}
print(c.subtract(sub))
print(c.most_common())


#5.OrderdDict
from collections import OrderedDict
d=OrderedDict()
d[1]='m'
d[2]='a'
d[3]='d'
d[4]='h'
d[5]='u'
print(d)
print(d.keys())
print(d.items())

#6.defaultdict
from collections import defaultdict
d=defaultdict(int)
d[1]='python'
d[2]='madhu'
print(d)
print(d[3])#### default value as 0

