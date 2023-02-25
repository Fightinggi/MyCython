from typing import Optional, Union, Callable


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:  # head : ListNode = None
        if not head or not head.next: return head
        p = self.reverseList(head.next)  # p 3  head 保存留到下一个递归
        head.next.next = head  # 2 的 next的next ==  3的next  指向了2节点 得到反转
        head.next = None
        return p  # 3 2


class LinkList:
    def __init__(self):
        self.head = None

    def initList(self, data):
        # 创建头结点
        self.head = ListNode(data[0])
        r = self.head
        p = self.head
        # 逐个为 data 内的数据创建结点, 建立链表
        for i in data[1:]:
            node = ListNode(i)
            p.next = node
            p = p.next
        return r

    def printlist(self, head):
        if head == None: return
        node = head
        while node != None:
            print(node.val, end='')
            node = node.next


def add(a: int, b: int) -> int:
    return a + b


def process(fn: Union[str, Callable]):
    if isinstance(fn, str):
        # str2fn and process

        print(fn)
        pass
    elif isinstance(fn, Callable):
        fn()


if __name__ == '__main__':
    l = LinkList()
    data1 = [1, 2, 3]
    data2 = [2, 4, 6]
    l1 = l.initList(data1)
    l2 = l.initList(data2)
    l.printlist(l1)

    s = Solution()
    p1 = s.reverseList(l1)

    l.printlist(p1)

    # a = 1
    # b = 2
    # add_ = add(a, b)
    #
    # print(process(add))
    # process("Union用法")
