# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 19:17:08 2016

@author: nathan
"""

class Vec:
    def __init__(self, labels, function):
        self.D = labels
        self.f = function
        
    def __repr__(self):
        return "%s %s" % (self.D, self.f)
        
    #def __str__(self):
    #    return 
        
    def zero_vec(D):
        return Vec(D, {})
        
    def setitem(v, d, val):
        v.f[d] = val
        
    def getitem(v,d):
        return v.f[d] if d in v.f else 0
        
    def scalar_mul(v, alpha):
        return Vec(v.D, {d:alpha * v.getitem(d) for d in v.D})
        
    def add(u, v):
        return Vec(u.D, {d:u.getitem(d) + v.getitem(d) for d in u.D})
        
            
        
v = Vec({'A','B','C'}, {'A':1})

v.setitem('B', 2)

print(v)

print(v.getitem('B'))

print(v.scalar_mul(2))

