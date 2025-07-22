# random number generation
import random

def getRandomNum(start,end):
    return random.randint(start,end)
a=getRandomNum(1,10)
print("random number is",a)

# is operator
a=[1,2,3]
b=[1,2,3]
c=a
print(a is b)
print(c is a)

# check if charecters are alphanumeric
def checkIfAlphaNum(inputEle):
    return inputEle.isalnum()
e=checkIfAlphaNum("123aaa")


# merge elements in sequence
def mergeEleInSeq(arrEle):
    return " ".join(arrEle)
temp_arr=['hello','world']
f=mergeEleInSeq(temp_arr)
print(f)