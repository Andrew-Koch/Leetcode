# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #Create a new linked list to store final result and pointer for node:
        sumList = ListNode(None)
        pointer = sumList
        carry = 0

        #For all values of linked list, sum values, including any carry over:
        while l1 or l2 or carry:
            #Get values of each list, sum values, add carry
            valOne, valTwo = l1.val if l1 else 0, l2.val if l2 else 0
            valSum = valOne + valTwo + carry
            #Calculate current node carry and LSD:
            lsd, carry = valSum % 10, valSum // 10
            
            #Save value to new linked list then go to next node:
            pointer.next = ListNode(lsd)
            pointer = pointer.next
            
            #If end of either list reached value is None:
            l1, l2 = l1.next if l1 else None, l2.next if l2 else None
        return sumList.next
