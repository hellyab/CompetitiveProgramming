def findMergeNode(head1, head2):
    foundIn1 = {}
    ctr = 0
    while head1 or head2:
        print(head1.data, head2.data)
        if head2.__hash__() in foundIn1:
            return head2.data
        else:
            foundIn1[head1.__hash__()] = True
            if ctr%2 == 0 and head1.next:
                head1 = head1.next
            elif ctr%2 == 0 and head2.next:
                head2 = head2.next
        ctr += 1