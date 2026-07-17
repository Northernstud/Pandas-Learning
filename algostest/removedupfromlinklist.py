# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



def deleteDuplicates(head: ListNode) -> ListNode:
    if head is None: 
         return None 
    
    b = head

    while b.next is not None: 
        if b.val == b.next.val:
            b.next = b.next.next
        else: 
            b = b.next

    return head

head = ListNode(1)

node1 = ListNode(1)

node2 = ListNode(2)

node3 = ListNode(3)

node4 = ListNode(3)

head.next = node1
node1.next = node2
node2.next = node3
node3.next = node4

def traverse(head):
        """Iterate and print every node from head to tail."""
        current = head  # 1. Start at the head node
        
        while current is not None:  # 2. Loop until reaching the end (None)
            print(current.val, end=" -> ")  # 3. Access data
            current = current.next  # 4. Move to the next node
            
        print("None")

print(traverse(deleteDuplicates(head)))
        