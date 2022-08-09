# a=[]
# print(a,type(a))

# p=["kompally",44]
# print(p,type(p))
# print(p[0],type(p[0]))
# print(p[1],type(p[1]))
# print(p[0],type(p[1]))
# print(p[2])   # IndexError: list index out of range

# a="hello"
# a[0]='H'
# print(type(a))
# print(a[0])  # h
# print(a[3])  # l
# print(a[-2]) # l
# print(a[7])  # IndexError: string index out of range

# a=None
# print(type(a))

# b=[6,5.8,'hi',None,True]
# print(b[0],type(b[0]))
# print(b[1],type(b[1]))
# print(b[2],type(b[2]))
# print(b[3],type(b[3]))
# print(b[4],type(b[4]))
# print(b[5],type(b[5]))  # Index Error: list index out of range

# r=[6,8.9,'python']
# r[0]=8
# r[-1]='hey'
# print(r)

# n=[1,8.0,'hey',[10,11]]
# print(n,type(n))
# print(n[0],type(n[0]))
# print(n[1],type(n[1]))
# print(n[2],type(n[2]))
# print(n[3],type(n[3]))
# print(n[3][0],type(n[3][0]))
# print(n[3][1],type(n[3][1]))

# m=[1,8.0,'hey',[10,11]]
# m[0]=45
# m[3][1]=12
# print(m,type(m))
# print(m[0],type(m[0]))
# print(m[1],type(m[1]))
# print(m[2],type(m[2]))
# print(m[3],type(m[3]))

# print(dir(list))

"""list methods"""
"""Append - It will add the elements at the end of the list"""
# n=[1,3.7,'hey',[1,10]]
# n.append(5)
# print(n
# print(n.append(5,6))

# m=[1,3.7,'hey',[1,10]]
# m.clear()
# print(m)

# n=[2,4,6,8]
# print(n)
# b=n.copy()
# print(b)

# n=[15,25,"hello",25,'']
# print(n.count(''))
# print(n.count(15))
# print(n.count(25))
# print(n.count('hi'))

# a=[20,40,60]
# b=[1,2,3,4]
# a.extend(b)
# print(a)
# b.extend(a)
# print(b)
# a=[20,40,60]
# b=1,2,3,4
# a.extend(b)
# print(a)

# n=[2,5,8,9,"hi",4.9,[46]]
# print(n.index(3.8))
# print(n.index(4.9))
# print(n.index([46]))
# print(n.rindex[2])  # AttributeError

# n=[2,4,6,8,10,12,14,16]
# n.insert(2,'heyy')
# n.insert(1,3)
# n.insert(-2,7)
# n.insert(-1,9)
# print(n)

# n=[10,20,30,40]
# print(n.pop())
# n=[10,20,30,40]
# n.pop()
# print(n)
# n.pop(0)
# print(n)

# n=[10,47,'hello',256,34]
# n.remove('hello')
# print(n)

# n=[1,2,3,4]
# print(n[::-1])
# n.reverse()
# print(n)

# n=[1,5,4,3,2]
# n.sort()
# print(n)
# n.sort(reverse=False)
# print(n)
# n.sort(reverse=True)
# print(n)

# j=[4.3,7.6,4.7,5.8]
# j.sort()
# print(j)

# k=['HD','LK','SL','HH','HA','s','BA','PA','DA','WM','LH','PZ']
# k.sort()
# print(k)
# d=['HD','LK','SL','HH','HA','S','BA','PA','DA','WM','LH','PZ']
# d.sort()
# print(d)