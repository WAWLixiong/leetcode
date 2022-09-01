class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        flag = False
        p1 = l1
        p2 = l2
        p = ListNode()
        h = p

        while p1 and p2:
            current = p1.val + p2.val
            if flag:
                current += 1
                flag = False
            if current >= 10:
                current = current % 10
                flag = True

            p.val = current
            if p1.next and p2.next:
                p.next = ListNode()
                p = p.next

            p1 = p1.next
            p2 = p2.next

        if not p1:
            p.next = p2
            m = p
            while p2:
                if flag:
                    m.next.val += 1
                    flag = False
                if m.next.val >= 10:
                    m.next.val = m.next.val % 10
                    flag = True
                p2 = p2.next
                m = m.next
        elif not p2:
            p.next = p1
            m = p
            while p1:
                if flag:
                    m.next.val += 1
                    flag = False
                if m.next.val >= 10:
                    m.next.val = m.next.val % 10
                    flag = True
                p1 = p1.next
                m = m.next
        if flag:
            m.next = ListNode(val=1)

        return h


if __name__ == '__main__':
    l1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
    l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))

    solution = Solution()
    ret = solution.addTwoNumbers(l1, l2)
    p = ret

    while p:
        print(p.val)
        p = p.next
