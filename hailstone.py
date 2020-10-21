"""
hailstone.py: Functions that will help with studying hailstone sequences
Author: Jonah Henry
"""
import timeit
result = []

#FUNCTION 1

def hailstone(n):
    if n == 1:
        result = n
    else:
        return n//2 if n % 2 == 0 else 3*n + 1

#FUNCTION 2

def hailstoneSeq(n):
    result = [n]
    while n != 1:
        n = hailstone(n)
        result.append(n)
    return result

#FUNCTION 3

def distanceToOne(n):
    result = 0
    while n != 1:
        n = hailstone(n)
        result += 1
    return result

def listHailstoneRecursive(n):
    pass
    print(n)
    if n > 0:
        if n == 1:
            print(n)
        elif n % 2 == 0:
            listHailstoneRecursive(n//2)
                


#Function 4

def listOddHails(n):
    result = hailstoneSeq(n)
    result = [i for i in result if i%2==1]
    return result

def averageOddRatio(n):
    odds = listOddHails(n)
    ratios = []
    for i in range(1,len(odds)-1):
        ratios.append(odds[i]/odds[i-1])
    result = sum(ratios)/len(ratios)
    return result

#Function 5

def reverseHailstone(n):
    return [2*n, (n-1)//3] if n % 6 == 4 else [2*n]


#Main

def main():
    reslst = []
    for i in range(3,100000):
        x = averageOddRatio(i)
        print(x)
        reslst.append(x)
    res = sum(reslst)/len(reslst)
    print(res)

main()


