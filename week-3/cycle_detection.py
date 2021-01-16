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