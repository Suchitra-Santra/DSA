# Definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head):
        dummy = ListNode(0)
        dummy.next = head
        current = dummy

        while current.next and current.next.next:
            first = current.next
            second = current.next.next

            # Swap the pair
            first.next = second.next
            second.next = first
            current.next = second

            # Move to the next pair
            current = first

        return dummy.next


# Function to create a linked list
def createLinkedList(arr):
    dummy = ListNode(0)
    current = dummy

    for num in arr:
        current.next = ListNode(num)
        current = current.next

    return dummy.next


# Function to print a linked list
def printLinkedList(head):
    while head:
        print(head.val, end=" -> " if head.next else "")
        head = head.next
    print()


# Test
arr = [1, 2, 3, 4]

head = createLinkedList(arr)

print("Original List:")
printLinkedList(head)

solution = Solution()
newHead = solution.swapPairs(head)

print("After Swapping:")
printLinkedList(newHead)