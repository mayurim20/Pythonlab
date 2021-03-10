def addstring(str):
    length=len(str)
    if length>2:
        if str[-3:]=='ing':
            str +='ly'
        else:
            str +='ing'
    return str
print(addstring('abc'))
print(addstring('abcde'))
print(addstring('studing'))


output:abcing
       abcdeing
       studingly
