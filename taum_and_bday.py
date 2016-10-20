#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    best_price = float('inf')
    b,w = raw_input().strip().split(' ')
    b,w = [long(b),long(w)]
    x,y,z = raw_input().strip().split(' ')
    x,y,z = [long(x),long(y),long(z)]
    
    cost_b = min(x, y + z)
    cost_w = min(y, x + z)
    
    best_price = min(best_price, b * cost_b + w * cost_w) 
    print best_price
