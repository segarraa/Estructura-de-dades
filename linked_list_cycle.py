class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycle(head: ListNode) -> bool:
    lent = head
    rapid = head

    while rapid is not None and rapid.next is not None:
        lent = lent.next
        rapid = rapid.next.next
        if lent is rapid:
            return True

    return False
