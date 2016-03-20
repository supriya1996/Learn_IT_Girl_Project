class Node:

    def_init_(self,data):
	  self.data = data
	  self.next = None

class LinkedList:
     
	 def_init_(self):
	      self.head = None                          #Function to initialize head
		  
	 def push(self,new_data):
	       new_node = Node(new_data)
		   new_node.next = self.head                #make next of new_node as head
		   self.head = new_node                     #move the head to point to new node
		   
		   
		   # Given a reference to the head of a list and a key,
           # delete the first occurence of key in linked list
    def deleteNode(self, key):
         
                                        
        temp = self.head          # Store head node(assume we have pointer to the first node)
 
        # If head node itself holds the key to be deleted
        if (temp is not None):
            if (temp.data == key):
                self.head = temp.next
                temp = None                        #free temp
                return
 
        # Search for the key to be deleted, keep track of the
        # previous node as we need to change 'prev.next'
        while(temp is not None):
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
 
        # if key was not present in linked list
        if(temp == None):
            return
 
        # Unlink the node from linked list
        prev.next = temp.next
 
        temp = None
 
 
    # Utility function to print the linked LinkedList
    def printList(self):
        temp = self.head
        while(temp):
            print (" %d" %(temp.data))
            temp = temp.next
			
llist = LinkedList()
llist.push(7)
llist.push(1)
llist.push(3)
llist.push(2)
 
print("Created Linked List: ")
llist.printList()
llist.deleteNode(1) 
print("\nLinked List after Deletion of 1:")
llist.printList()