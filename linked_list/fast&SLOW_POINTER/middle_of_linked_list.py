class LinkedList:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next 




def middle_of_linked_list(head):
    slow=head
    fast=head 

    while(fast!=None and fast.next!=None):
        slow=slow.next 
        fast=fast.next.next

    current=slow

    while current!=None:
        print(current.val)
        current=current.next



if __name__=="__main__":

    node1=LinkedList(1)
    node2=LinkedList(2)
    node3=LinkedList(3)
    node4=LinkedList(4)
    node5=LinkedList(5)

    node1.next=node2
    node2.next=node3
    node3.next=node4 
    node4.next=node5 
    node5.next=None 

    head=node1


    print("The Middle of the Linked List Start From:", middle_of_linked_list(head))




    """

    Middle of the Linked List – Short Explanation

Problem:
Given the head of a singly linked list, find and return the middle node.

Important rule:
- If the list has an odd number of nodes, return the single middle node.
- If the list has an even number of nodes, return the SECOND middle node.

Example:
1 -> 2 -> 3 -> 4 -> 5
Middle = 3

1 -> 2 -> 3 -> 4 -> 5 -> 6
Two middle nodes are 3 and 4.
We return 4.

Approach: Slow and Fast Pointers

Use two pointers:
- slow moves one node at a time.
- fast moves two nodes at a time.

Initially:
slow = head
fast = head

Keep moving them while:
fast != None and fast.next != None

Inside the loop:
slow = slow.next
fast = fast.next.next

When the loop ends, slow will be pointing to the middle node.

Why does it work?
Fast moves twice as quickly as slow. Therefore, when fast reaches the end of the linked list, slow has travelled approximately half of the list. That means slow is at the middle.

Dry Run:
List:
1 -> 2 -> 3 -> 4 -> 5

Start:
slow = 1
fast = 1

Step 1:
slow = 2
fast = 3

Step 2:
slow = 3
fast = 5

Now fast.next is None, so the loop stops.

slow = 3
Therefore, 3 is the middle node.

For an even list:
1 -> 2 -> 3 -> 4 -> 5 -> 6

Start:
slow = 1, fast = 1

Step 1:
slow = 2, fast = 3

Step 2:
slow = 3, fast = 5

Step 3:
slow = 4, fast = None

The loop stops and slow points to 4, which is the second middle node.

Complexity:
Time Complexity: O(n)
The list is traversed once.

Space Complexity: O(1)
Only slow, fast, and possibly one temporary pointer are used. No extra array/list is required.

Key Pattern to Remember:
slow -> 1 step
fast -> 2 steps

When fast reaches the end:
slow -> middle
    
    
    
    
    
    
    """