# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 18:48:05 2019

@author: 10539
"""

class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
        
class binsearch_tree:
    def __init__ (self,val):
        self.start=Node(val)
        
    def search(self,val):
        root= self.start
        while root:
            if val==root.val:return True
            elif  val<root.val:root=root.left
            else:root=root.right
        return False

    def findMin(self, root):
        if root.left:
            return self.findMin(root.left)
        else:
            return root
    
    def insert(self, root, val):
        if root == None:
            root = Node(val)
        elif val < root.val:
            root.left = self.insert(root.left, val)
        elif val > root.val:
            root.right = self.insert(root.right, val)
        return root
        
    
    def delete(self, root, val):
        if root == None:
            return 
        if val < root.val:
            root.left = self.delete(root.left, val)
        elif val > root.val:
            root.right = self.delete(root.right, val)
        else:
            if root.left and root.right:
                temp = self.findMin(root.right)
                root.val = temp.val
                root.right = self.delete(root.right, temp.val)
            elif root.right == None and root.left == None:
                root = None
            elif root.right == None:
                root = root.left
            elif root.left == None:
                root = root.right
        return root

    def pre_tran(self):
        stack=[]
        root=self.start
        while root:
            print(root.val)
            if root.left!=None:
                stack.append(root)
                root=root.left
            else:
                if root.right!=None:
                    root=root.right
                else:
                    if stack:
                        ll=stack[-1]
                        while stack and ll.right==None:
                            ll=stack[-1]
                            stack.pop()                        
                        root=ll.right
                    else:
                        break
                    
    def mid_tran(self,root):#开始的时候输入self.start
         if root==None:
             return
         self.mid_tran(root.left)
         print(root.val)
         self.mid_tran(root.right)
         
    def post_tran(self,root):
        if root==None:
            return
        self.mid_tran(root.left)
        self.mid_tran(root.right)
        print(root.val)
             

    def layer_tran(self):
        if self.start== None:
            return
        queue = []
        queue.append(self.start)
        while queue:
            currentNode = queue.pop(0)
            print(currentNode.val, end=' ')
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)


lala=binsearch_tree(8)
lala.insert(lala.start,1)
lala.insert(lala.start,88)
lala.insert(lala.start,6)
lala.insert(lala.start,4)
lala.layer_tran()
          
                
''' 从start开始，print ,left!=None->append root &root=root.left
                           left==None->if right!=None:root=root.right
                                       if right==None:if stack:ll=stack[-1]
                                                               while stack and ll.right==None:
                                                                 stack.pop()
                                                                 ll=stack[-1]
                                                                if stack:stack.pop()&root=ll.right
                               
       
'''
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
            