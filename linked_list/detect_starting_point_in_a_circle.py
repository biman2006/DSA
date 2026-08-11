class LinkedList:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next 




def detect_starting_point_of_cycle(head):
    slow=head
    fast=head 

    while(fast!=None and fast.next!=None):
        slow=slow.next
        fast=fast.next.next

        if slow==fast:
            slow=head
            index=0

            while(slow!=fast):
                slow=slow.next
                fast=fast.next 
            return slow, index
    else:
      return -1



if __name__=="__main__":
    node1=LinkedList(4)
    node2=LinkedList(2)
    node3=LinkedList(1)
    node4=LinkedList(23)
    node5=LinkedList(10)

    node1.next=node2 
    node2.next=node3 
    node3.next=node4 
    node4.next=node5 
    node5.next=node3 

    head=node1 

    res,index=detect_starting_point_of_cycle(head)

    if res is not -1:
        print("Cycle find at:", res.val)
        print("AT index:", index)
    else:
        print("No CYCLE")




"""

NOTE:

Cycle Detection & Starting Point:

Detection: By moving a slow pointer one step at a time and a fast pointer two steps at a time, you can determine if a loop exists. If they meet, a cycle is present.
Finding the Entry: Once a cycle is detected, resetting the slow pointer to the head and moving both pointers one step at a time will cause them to meet exactly at the cycle's starting node. This works because the distance from the head to the entry point is equal to the distance from the meeting point to the entry point within the cycle.
Finding the Middle of a Linked List:

This pattern also helps identify the middle node without needing to know the list's total length in advance.
By moving the fast pointer at twice the speed of the slow pointer, the fast pointer reaches the end of the list while the slow pointer arrives exactly at the middle. This allows for finding the middle node in a single traversal.



MATHEMATICAL LOGIC:


The mathematical intuition behind finding the starting point of a cycle in a linked list involves understanding the distances covered by the slow and fast pointers until they meet.

Defining Variables
**L1: Distance from the head to the entry point.
**L2: Distance from the entry point to the meeting point.
**C: Total number of nodes in the cycle.

The Mathematical Logic
When the pointers meet at the meeting point, the total distance covered by each can be represented as:

**Slow pointer distance: L1+L2
Fast pointer distance: L1+L2+nC
 
 (
 where n
 is the number of loops the fast pointer completed in the cycle).
Since the fast pointer moves at twice the speed of the slow pointer, we equate them:
 **2(L1+L2)=L1+L2+nC
Solving for 
L1:
2L1+2L2=L1+L2+nC
L1=nC-L2



What This Means
This equation implies that the distance from the head to the entry point (L1) is equal to the distance from the meeting point to the entry point (C-L2)
.




Time Complexity: O(n) 
Space Complexity: O(1) 







"""
    

