  #Binary search Tree creation and  search program
  

class Node:


     def_init_(self,key):
	      self.left = None
		  self.right = None
		  self.val = key
		  

root = Node(50)                              #create root

  #Binary tree creation
root.left = Node(30)              
root.right = Node(70)

root.left.left = Node(20)
root.left.right = Node(40)
root.right.left = Node(60)
root.right.right = Node(80)

		  #function to search a key
     def search(root,key):
	      if root is None or root.val == key:
		       return root
		  if root.val < key:
		       return search(root.right,key)
			   
		  return search(root.left,key)
	