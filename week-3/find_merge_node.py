def findMergeNode(head1, head2):
    foundIn1 = {}
    while head1 or head2:
        print(head1.data, head2.data)
        if head2.__hash__() in foundIn1:
            return head2.data
        else:
            foundIn1[head1.__hash__()] = True
            if head1.next:
                head1 = head1.next
            elif head2.next:
                head2 = head2.next

def findMergeNode2(head1, head2):
    h1_stack = []
    h2_stack = []
    while head1:
        h1_stack.append(head1)
        head1 = head1.next
    while head2:
        h2_stack.append(head2)
        head2 = head2.next
    merge_node = h2_stack[-1]
    while h2_stack and h1_stack and h1_stack[-1] == h2_stack[-1] :
        merge_node = h1_stack[-1]
        h1_stack.pop()
        h2_stack.pop()
    return merge_node.data