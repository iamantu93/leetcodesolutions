class Solution:
    # https://leetcode.com/problems/remove-nth-node-from-end-of-list/
    def removeNthFromEnd(self, head, n):
        def index(node):
            if not node:
                return 0
            i = index(node.next) + 1
            if i > n:
                node.next.val = node.val
            return i
        index(head)
        return head.next

