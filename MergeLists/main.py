class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = ListNode(val=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = ListNode(val=elem)
                node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.val))
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)


class Solution:
    def mergeTwoLists(self, l1, l2):

        def Merge(A, X, Y):
            i = 0
            while len(X) > 0 and len(Y) > 0:
                A[i] = X.pop(0) if X[0] < Y[0] else Y.pop(0)
                i += 1
            A[i:] = X if len(X) > 0 else Y
            return A

        def Sort(A):
            if len(A) > 1:
                m = len(A) // 2
                X = [x for x in A[:m]]
                Y = [y for y in A[m:]]
                X = Sort(X)
                Y = Sort(Y)
                A = Merge(A, X, Y)
            return A

        first = []
        second = []
        cur1 = l1.head
        cur2 = l2.head
        while cur1 is not None:
            first.append(cur1.val)
            cur1 = cur1.next
        while cur2 is not None:
            second.append(cur2.val)
            cur2 = cur2.next
        A = first + second
        res = LinkedList(Sort(A))
        return res


l1, l2 = LinkedList([1, 2, 4]), LinkedList([1, 3, 4])
test = Solution()
node = test.mergeTwoLists(l1, l2)
print(node.__repr__())
