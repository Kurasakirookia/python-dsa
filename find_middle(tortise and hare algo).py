#own
def find_middle(self):
        n=self.length%2
        rem=self.length//2
        if n==0:
            return self.get(rem).value
        else:
            return self.get(rem).value
#tortise and hare algorithm 
def find_middle(self):
    slow = self.head
    fast = self.head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow