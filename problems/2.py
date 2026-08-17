class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        dummy = ListNode()
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry

            carry = total // 10
            digit = total % 10

            current.next = ListNode(digit)
            current = current.next

            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

        return dummy.next


if __name__ == "__main__":
    l1_list = [2, 4, 3]
    l2_list = [5, 6, 4]

    l1 = [ListNode(i) for i in l1_list]
    l2 = [ListNode(j) for j in l2_list]

    for i in range(len(l1_list) - 1):
        l1[i].next = l1[i+1]

    for j in range(len(l2_list) - 1):
        l2[j].next = l2[j + 1]

    solution = Solution()
    # logger.info(solution.twoSum(nums=nums, target=target))
    print(solution.addTwoNumbers(l1=l1[0], l2=l2[0]))