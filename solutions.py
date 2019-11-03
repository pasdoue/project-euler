#!/usr/bin/python

#01
def multiple_of_5_and_3(limit=1000):
    total_sum=5+3
    for x in xrange(6,limit):
        if x%3==0 or x%5==0:
            total_sum+=x
    print total_sum

#02
def fibonacci_even(limit=4000000):
    a=1
    b=2
    c=a+b
    total_sum=b
    while c < limit:
        c=a+b
        a=b
        b=c
        if b%2==0:
            total_sum+=b
    print total_sum


fibonacci_even()

