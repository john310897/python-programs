import copy
a=[[1,3],[2,10]]

#deep copy
c=copy.deepcopy(a)
c[0][0]=0
print("deep copy output",c,a)

# shallow copy
b=a.copy()
b[0][0]=0
print("shallow copy output",b,a) #changes the main variable to
