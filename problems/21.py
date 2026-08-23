class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(
        self, list1: ListNode | None, list2: ListNode | None
    ) -> ListNode | None:

        dummy = ListNode()
        current = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next

            current = current.next

        if list1:
            current.next = list1
        else:
            current.next = list2

        return dummy.next

if __name__ == "__main__":
    l1_list = [1, 2, 4]
    l2_list = [1, 3, 4]

    l1 = [ListNode(i) for i in l1_list]
    l2 = [ListNode(j) for j in l2_list]

    for i in range(len(l1_list) - 1):
        l1[i].next = l1[i + 1]

    for j in range(len(l2_list) - 1):
        l2[j].next = l2[j + 1]

    solution = Solution()
    # logger.info(solution.twoSum(nums=nums, target=target))
    print(solution.mergeTwoLists(list1=l1[0], list2=l2[0]))