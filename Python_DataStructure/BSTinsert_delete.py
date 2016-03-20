class Node: 
     def_init_(self,key):
	      self.left = None
		  self.right = None
		  self.val = key
	 def inorder(root):
	      if root is not None:
		       inorder(root.left)
			   print(root.key)
			   inorder(root.right)
	 def insert(root,node):
	      if root is None:
		      root = node
		  if root.val < key:
		      if root.right = None:
			     root.right = node
			  else:
			     insert(root.right,node)
		  else:
		       if root.left = None:
			        root.left = node
			   else:
			       insert(root.left,node)
				   
	 def deleteNode(root,key):
	  
	       if root is None:
		        return Node
		   if Key < root.key:
		       root.left = deleteNode(root.left,key)
		   elif key > root.key:
		       root.right = deleteNode(root.right,key)
			   
			   #Node with one child or no child
		   else:
		         if root.left is None:
				          temp = root.right
				          root = None
						  return temp
				 elif root.right is None:
				          temp = root.left
						  root = None
						  return temp
			   
				 # Node with two children
              
                temp = minValueNode(root.right)
 
                 # Copy the inorder successor's content to this node
				 
                root.key = temp.key
 
                 # Delete the inorder successor
				 
                root.right = deleteNode(root.right , temp.key)
				
			return root
  
  #program to insertion and deletion(implement)
  
root = None
root = insert(root, 50)
root = insert(root, 30)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 70)
root = insert(root, 60)
root = insert(root, 80)
 
print "inorder traversal of the given tree"
inorder(root)
 
print "\nDelete 20"
root = deleteNode(root, 20)

print "Inorder traversal of the modified tree"
inorder(root)
 
print "\nDelete 30"
root = deleteNode(root, 30)

print "Inorder traversal of the modified tree"
inorder(root)
 
print "\nDelete 50"
root = deleteNode(root, 50)

print "Inorder traversal of the modified tree"
inorder(root)
 
			   