class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head

        fast = dummy
        slow = dummy

        for _ in range(n + 1):
            fast = fast.next

        while fast:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return dummy.next


def create_list(arr):
    dummy = ListNode()
    curr = dummy
    for x in arr:
        curr.next = ListNode(x)
        curr = curr.next
    return dummy.next


def print_list(head):
    while head:
        print(head.val, end=" ")
        head = head.next
    print()


arr = list(map(int, input("Enter linked list values: ").split()))
n = int(input("Enter n: "))

head = create_list(arr)

sol = Solution()
result = sol.removeNthFromEnd(head, n)

print("Updated list:")
print_list(result)