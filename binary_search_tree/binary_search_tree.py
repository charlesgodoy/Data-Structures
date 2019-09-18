# import sys
# sys.path.append('../queue_and_stack')
# from dll_queue import Queue
# from dll_stack import Stack

# Questions:
# Only ints?
# Negative numbers?

#Observations
# >= goes right
# 

class BinarySearchTree:
  def __init__(self, value):  # Just using value, so key is value
    self.value = value
    self.left = None
    self.right = None

    # *'insert' adds the input value to the binary search tree, adhearing to the
    # rules of the ordering of elements in a binary search tree.
    # Need to traverse to find spot to insert

  def insert(self, value):
    root = self
    if value < root.value:
      if root.left is None:
        root.left = BinarySearchTree(value)

      else:
        root.left.insert(value)

    else:
      if root.right is None:
        root.right = BinarySearchTree(value)

      else:
        root.right.insert(value)

    # * 'contains' searches the binary search tree for the input value,
    # returning a boolean indicating wheather the value exists in the tree or not
    # Start from the root and traverse the tree
    # We can stop at the first instance of a value
    # We know it's not found if we get to a node that doesn't have children

  def contains(self, target):

    root = self
    target = target
    
    if root is None or root.value == target:
      return root

    if root.value < target:
      return BinarySearchTree.contains(root.right, target)

    return BinarySearchTree.contains(root.left, target)

    # 'get_max' returns the maximum value in teh binary search tree
  def get_max(self):
    node = self

    while node.right is not None:
      node = node.right

    return node.value

    # * 'for_each' performs a traversal of _every_ node in the tree, executing
    # the passed-in callback function on each tree node value. There is a myriad of ways to
    # perform tree traversal; in this case any of them should work.
  def for_each(self, cb):
    node = self
    cb(node.value)
    if node.left:
      node.left.for_each(cb)
      
    if node.right:
      node.right.for_each(cb)