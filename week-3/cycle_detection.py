def has_cycle(head):
    foundMap = {}
    while head:
        if head.next == None:
            return 0
        elif head.__hash__() in foundMap:
            return 1
        foundMap[head.__hash__()] = True
        head = head.next
    return 0

def has_cycle2(head):
    slow = head
    fast = head
    while fast:
        if fast == slow:
            return 1
        if not fast.next:
            return 0
        fast = fast.next.next
        slow = slow.next
    return 0 