## import modules here 
import copy
import math
from collections import  deque

################# Question 0 #################

def add(a, b): # do not change the heading of the function
    return a + b


################# Question 1 #################

def nsqrt(x):# do not change the heading of the function
    if x <=0:
        return
    else:
        a = 1
        b = x + 0.25
        t = 0
        mid = (a + b) / 2
        while True:
            if (mid * mid - x) * (a * a - x) <= 0:
                b = mid
            else:
                a = mid
            lastmid = mid
            mid = ((a + b) / 2)
            # print(a,b)
            if abs(mid - lastmid) <= 0.1:
                break
        return (round(lastmid))



'''
        mid = int((a + b)/2)
        midmid=mid*mid

        if midmid-x>=0 and t==0:
            b=(mid)
            continue
        else:
            t=1

            if midmid >= x:
                print(answer)
                print(mid)
                break
            else:
                a = (mid)
                answer = copy.copy(mid)

        print(mid,a,b)
'''


################# Question 2 #################


# x_0: initial guess
# EPSILON: stop when abs(x - x_new) < EPSILON
# MAX_ITER: maximum number of iterations

## NOTE: you must use the default values of the above parameters, do not change them

def find_root(f, fprime, x_0=1.0, EPSILON = 1E-7, MAX_ITER = 1000): # do not change the heading of the function
    iter=0
    if f(x_0)==0:
        return 0
    while iter<=MAX_ITER:
        m = f(x_0)/fprime(x_0)
        x_1 = x_0 - m
        absff = abs(x_0 - x_1)
        if absff < EPSILON:
            return x_1
        else:
            x_0 = x_1
            iter+=1
    return x_1



    ################# Question 3 #################
class Tree(object):
    def __init__(self, name='ROOT', children=None):
        self.name = name
        self.children = []
        if children is not None:
            for child in children:
                self.add_child(child)
    def __repr__(self):
        return self.name
    def add_child(self, node):
        assert isinstance(node, Tree)
        self.children.append(node)

def print_tree(root, indent=0):
    print(' ' * indent, root)
    if len(root.children) > 0:
        for child in root.children:
            print_tree(child, indent+4)

def make_tree(tokens):
    stack=[]
    for i in tokens:
        stack.append(i)
        #print(stack)
        if i == ']':
            L=[]
            while stack[-1]!='[':
                a=stack.pop()
                L.append(a)
            L.append(stack.pop())
            L.append(stack.pop())
            #print(L)
            L.reverse()
            #print(L)
            tree = Tree(L[0])
            for i in range(1,len(L)):
                if L[i] == ']' or L[i]=='[':
                    pass
                else:
                    if type(L[i])==Tree:
                        tree.add_child(L[i])
                    else:
                        tree.add_child(Tree(L[i]))
            #print_tree(tree)
            stack.append(tree)
    return tree






def max_depth(root): # do not change the heading of the function
    if root == None:# **replace** this line with your code
        return 0
    maxdepth=0
    L=[]
    v=[]
    L.append(root)
    v.append(root)
    while len(L) > 0:
        x = L[-1]
        for i in  range(0,len(x.children)):
            if not x.children[i] in v:
                v.append(x.children[i])
                L.append(x.children[i])
                break
        if maxdepth <= len(L):
            maxdepth=len(L)
            #print(maxdepth)
            #print(L[-1].children)
        if L[-1]== x:
            L.pop()
    return maxdepth
