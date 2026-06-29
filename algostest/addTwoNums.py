#You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

#You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# Definition for singly-linked list.


# First medium ez could be better but imma find better solution later. 
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        n1 = 0 
        i = 1
        n2 = 0 

        while l1 is not None or l2 is not None:

            if l1 is not None:
                n1 = l1.val * i + n1
                l1 = l1.next

            if l2 is not None:
                n2 = l2.val * i + n2
                l2 = l2.next

            i *= 10

        def flipnum(n) -> ListNode: 
            if n == 0:
                return ListNode(0)
            
            root = ListNode()
            a = root

            while n != 0:
                a.next = ListNode(n % 10)
                a = a.next
                n = n // 10

            return root.next
        

        return(flipnum(n1 + n2))


def create_list_from_array(ar) -> ListNode:
    if not ar:
        return None

    head = ListNode(ar[0])
    current = head

    for val in ar[1:]:
        current.next = ListNode(val)
        current = current.next

    return head



sol = Solution()
# sol.addTwoNumbers(root, root)

def ListNodeTrav(root):
    while root is not None: 
        print(root.val)
        root = root.next


a = sol.addTwoNumbers(create_list_from_array([2, 4, 3, 8, 8]), create_list_from_array([5,6,4]))

ListNodeTrav(a)

                

