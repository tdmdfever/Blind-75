"""
Given the head of a Singly LinkedList, write a function to determine if the 
LinkedList has a cycle in it or not.
"""

class Node:
    def __init__(self, value, next=None):
        self.val = value
        self.next = next
