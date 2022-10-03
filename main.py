#Solve Problems using loops
#1
# n = int(input("Enter number: "))
# for i in range(1, n + 1):
#     print("Number is :", i, "and cube of the", i, "is :", i**3 )

#2
# A = input("Enter number:").split()
# A.reverse()
# print(A)

#3
# n = int(input("Enter number: "))
# factorial = 1
# while n > 1:
#    factorial = n * factorial
#    n = n - 1
# print(factorial)

#4
# s = int(input("Enter: "))
# x = 1
# while s > 1:
#    x = s + x
#    s = s - 1
# print(x)

#5
# def getPalindrom(text):
#     if text == text[::-1]:
#         return True
#     return False
#
# print(getPalindrom(input("Enter: ")))

#Solve Problems using nested loops
#1

# n = int(input("Enter the number of lines:"))
# for i in range(0, n + 1):
#     for x in range(n - i, 0, -1):
#         print(x, end=' ')
#     print()

#2
# n = int(input("Enter the number of lines:"))
# for i in range(n+1):
#     for x in range(i):
#         print(i, end=' ')
#     print('')

#Solve problems using regular or lambda functions

#1
# get_Discount = lambda f,s: f-(f/100*s)
# sum = get_Discount(*map(int,input("Enter numbers: ").split()))
# print(sum)

#2
# def sum_numbers(n):
#     if n == 0:
#         return 0
#     else:
#         return n+sum_numbers(n-1)
# print(sum_numbers(int(input("Enter number: "))))
#

# def is_triplet(a,b,c):
#     if (a**2)+(b**2)==(c**2) or (a**2)+(c**2)==(b**2) or (c**2)+(b**2)==(a**2):
#         print("True")
#     else:
#         print("False")
# is_triplet(a = int(input("a: ")),b = int(input("b: ")),c = int(input("c: ")))