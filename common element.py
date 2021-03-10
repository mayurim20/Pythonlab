a=[2,3,4,5,6]
b=[3,6,9,8,1]
def common(a,b):
    c=[value for value in a if value in b]
    return c
d=common(a,b)
print(d)
