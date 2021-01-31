# 雙指針法 時:O(N) 空:O(1)
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        cur = head
        pre = None
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre
        
# 遞歸解法 時:O(N) 空:O(N)    
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre = None
        cur = head
        def reverse(pre, cur):
            if cur is None:
                return pre
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
            return reverse(pre, cur)
        return reverse(pre, cur)
