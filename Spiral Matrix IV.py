0# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def insert_end(root, item):
    temp = ListNode(val=item)
    if root is None:
        return temp

    last = root
    while last.next is not None:
        last = last.next

    last.next = temp
    return root


def array_to_linked_list(arr):
    root = ListNode()
    for item in arr:
        root = insert_end(root, item)
    return root


class Solution:
    def spiralMatrix(self, m: int, n: int, head: ListNode):
        mat = [[-1] * n for _ in range(m)]
        d = [0, 1]
        i, j = 0, 0
        head = head.next
        while head is not None:
            print(d)
            if (j == n - 1 and i < m-1) or mat[i][j + 1] != -1:
                d = [1, 0]
            elif (i == m - 1 and j < n-1) or mat[i + 1][j] != -1:
                d = [0, -1]
            elif (j == 0 and i > 0) or mat[i][j + 1] != -1:
                d = [-1, 0]
            elif (i == 0 and j > 0) or mat[i + 1][j] != -1:
                d = [0, 1]

            mat[i][j] = head.val

            head = head.next
            i += d[0]
            j += d[1]

        return mat


linked_list = array_to_linked_list([3, 0, 2, 6, 8, 1, 7, 9, 4, 2, 5, 5, 0])
print(Solution().spiralMatrix(3, 5, linked_list))
