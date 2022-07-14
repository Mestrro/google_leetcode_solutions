# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from Queue import PriorityQueue
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        amount = len(lists)
        interval = 1
        while interval < amount:
            for i in range(0, amount - interval, interval * 2):
                lists[i] = self.merge2Lists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0] if amount > 0 else None
    def merge2Lists(self, list1, list2):
        head = point = ListNode(0)
        while list1 and list2:
            if list1.val <= list2.val:
                point.next = list1
                list1 = list1.next
            else:
                point.next = list2
                list2 = list1
                list1 = point.next.next
            point = point.next
        if not list1:
            point.next = list2
        else:
            point.next = list1
        return head.next
