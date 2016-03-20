
# insertion methods of linked list
 

class Node:
 
    # Function to initialise the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null
 
 
#
class LinkedList:
 
    # Function to initialize head
    def __init__(self):
        self.head = None
 
 
    # Function to insert a new node at the beginning
    def push(self, new_data):
 
       
        new_node = Node(new_data)
 
                                             
        new_node.next = self.head                # Make next of new Node as head
 
        
        self.head = new_node                      # Move the head to point to new Node
 
 
    # Insert new node after given node
    def insertAfter(self, prev_node, new_data):
 
        # check if the given prev_node exists
        if prev_node is None:
            print("The given previous node must inLinkedList.")
            return
 
        
       
        new_node = Node(new_data)              #allocate data to new node
 
        # Make next of new Node as next of prev_node
        new_node.next = prev_node.next
 
        #  make next of prev_node as new_node
        prev_node.next = new_node
 
 
    
    # Appends a new node at the end. 
    
    def append(self, new_data):
 
        # 1. Create a new node,put in the data and set next as none
        
        
        new_node = Node(new_data)
 
        #If the Linked List is empty, then make the
        #new node as head
        if self.head is None:
            self.head = new_node
            return
 
        # Else traverse till the last node
        last = self.head
        while (last.next):
            last = last.next
 
        #Change the next of last node
        last.next =  new_node
 
 
    #  function to print the linked list
    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next
 
 
 
# Code execution starts here
if __name__=='__main__':
 
    # Start with the empty list
    llist = LinkedList()
 
    # Insert 6.  So linked list becomes 6->None
    llist.append(6)
 
    # Insert 7 at the beginning. So linked list becomes 7->6->None
    llist.push(7);
 
    # Insert 1 at the beginning. So linked list becomes 1->7->6->None
    llist.push(1);
 
    # Insert 4 at the end. So linked list becomes 1->7->6->4->None
    llist.append(4)
 
    # Insert 8, after 7. So linked list becomes 1 -> 7-> 8-> 6-> 4-> None
    llist.insertAfter(llist.head.next, 8)
 
    print('Created linked list is:')
    llist.printList()
 

