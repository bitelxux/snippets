#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    min_price = 10**1000
    b,w = raw_input().strip().split(' ')
    b,w = [long(b),long(w)]
    x,y,z = raw_input().strip().split(' ')
    x,y,z = [long(x),long(y),long(z)]
    
    cb = min(x, y + z)
    cw = min(y, x + z)
    
    min_price = min(min_price, b * cb + w * cw) 
    print min_price
