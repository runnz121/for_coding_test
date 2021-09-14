#Definition for singly-linked list.
#from platform import node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        prev = None

        while node:
            next = node.next
            print('next : ', {next})

            node.next = prev
            print('prev : ', {prev})

            prev = node
            print('node : ', {node})
            node = next

        return prev

    # next: {ListNode{val: 2, next: ListNode{val: 3, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}}}
    # prev: {None}
    # node: {ListNode{val: 1, next: None}}

    # next: {ListNode{val: 3, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}}
    # prev: {ListNode{val: 1, next: None}}
    # node: {ListNode{val: 2, next: ListNode{val: 1, next: None}}}

    # next: {ListNode{val: 4, next: ListNode{val: 5, next: None}}}
    # prev: {ListNode{val: 2, next: ListNode{val: 1, next: None}}}
    # node: {ListNode{val: 3, next: ListNode{val: 2, next: ListNode{val: 1, next: None}}}}

    # next: {ListNode{val: 5, next: None}}
    # prev: {ListNode{val: 3, next: ListNode{val: 2, next: ListNode{val: 1, next: None}}}}
    # node: {ListNode{val: 4, next: ListNode{val: 3, next: ListNode{val: 2, next: ListNode{val: 1, next: None}}}}}

    # next: {None}
    # prev: {ListNode{val: 4, next: ListNode{val: 3, next: ListNode{val: 2, next: ListNode{val: 1, next: None}}}}}
    # node: {ListNode{val: 5, next: ListNode{val: 4, next: ListNode{val: 3, next: ListNode{val: 2, next: ListNode{val: 1, next: None}}}}}}