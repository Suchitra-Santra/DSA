import heapq

# Definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists):
        heap = []

        # Add first node of each list to heap
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        dummy = ListNode(0)
        current = dummy

        while heap:
            val, i, node = heapq.heappop(heap)

            current.next = node
            current = current.next

            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next


# Function to create linked list
def createLinkedList(arr):
    dummy = ListNode(0)
    current = dummy

    for num in arr:
        current.next = ListNode(num)
        current = current.next

    return dummy.next


# Function to print linked list
def printList(head):
    while head:
        print(head.val, end=" ")
        head = head.next


# Test case
list1 = createLinkedList([1, 4, 5])
list2 = createLinkedList([1, 3, 4])
list3 = createLinkedList([2, 6])

lists = [list1, list2, list3]

solution = Solution()
result = solution.mergeKLists(lists)

print("Merged list:")
printList(result)