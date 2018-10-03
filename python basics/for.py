# basic
# for i in range(11):
#     print(i)

#Wap to take start point and end point from user and print the range.
# num1=int(input('Enter first num : '))
# num2=int(input('Enter second num : '))
#
# for i in range (num1,num2):
#     print(i)


# with offset
# num1=int(input('Enter first num : '))
# num2=int(input('Enter second num : '))
# num4=int(input('Enter the offset number : '))
# num3=range(num1,num2,num4)
# print(*num3)

# reverse
# num1=int(input('Enter first num : '))
# num2=int(input('Enter second num : '))
# num4=int(input('Enter the offset number : '))
# num3=range(num1,num2,num4)
# print(*num3)


# Wap to print fibonacci series.

# num=int(input('Enter first number : '))
# a=0
# b=1
# print(a)
# print(b)
# for i in range(num):
#     c=a+b
#     a=b
#     b=c
#     print(c)

#Wap to find the factorial of a given number.

num=int(input('Enter the number : '))
res=1
for i in range(1,num+1):
    res=res*i
print(res)