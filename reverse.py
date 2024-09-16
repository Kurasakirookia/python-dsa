def reverse(self):
    if self.head is None:
        return "Empty list"

    prev = None
    current = self.head
    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    self.head = prev
    temp_node = self.head
    result = ''
    while temp_node is not None:
        result += str(temp_node.value)
        if temp_node.next is not None:
            result += ' -> '
        temp_node = temp_node.next
    #
    return self