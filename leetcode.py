class Solution:
    def reverse(self, x: int) -> int:
        x = [i for i in str(x)]
        x.reverse()
        x = int(''.join(x))
        small = 2**-32
        big = 2**32
        if x >= big or x <= small:
            return 0 
        return 

class ListNode:     
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
 
def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    merged_list = []
    while True:
        merged_list.extend([l1.val, l2.val])
        if not l1.next or not l2.next:
            break
        l1 = l1.next
        l2 = l2.next
    for var in merged_list:
        base_node = ListNode()
        base_node.val = var
        base_node.next = ListNode()
        base_node = base_node.next
    return base_node

if __name__ == '__main__':
    l1 = ListNode(val = 1, next = ListNode(val = 2, next = ListNode(val = 4, next =None)))
    l2 = ListNode(val= 1, next= ListNode(val= 3, next= ListNode(val = 4, next = None)))
    print(mergeTwoLists(l1, l2))