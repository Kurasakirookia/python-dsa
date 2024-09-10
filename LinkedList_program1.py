class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' -> '
            temp_node = temp_node.next
        return result
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        
    def  get(self,index):
        temp=self.head
        if index>self.length-1 or index<0:
            return "list is empty"
        
        for _ in range(index):
            temp=temp.next
        return temp
    def pop_first(self):
        popednode=self.head
        if self.length==0:
            return None
        elif self.length==1:
            self.head=None
            self.tail=None
            
            
        else:
            
            self.head=self.head.next
            popednode.next=None
        self.length-=1
        return popednode
        
        
    def pop(self):
        temp=self.head
        popednode=self.tail
        if self.head==None:
            return None
        elif self.length==1:
            self.head=None
            self.tail=None
            
        else:
            while temp.next != self.tail:
                temp=temp.next
            
            temp.next=None
            self.tail=temp
        self.length-=1 
        return popednode
        
            
            
            
    def remove(self,index):
        if self.head==None:
            return None
        if index ==0:
            
            return self.pop_first()
            
        elif index<0 or index>=self.length:
            return "length of index exceeds"
        elif index==(self.length)-1:
           
            return self.pop()
            
        else:    
            prev=self.get(index-1)
            popednode=prev.next
            prev.next=popednode.next
            popednode.next=None
        self.length-=1
        return popednode
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
    
    def find_middle(self):
        n=self.length%2
        rem=self.length//2
        if n==0:
            return self.get(rem).value
        else:
            return self.get(rem).value
            
    def remove_duplicates(self):
        # TODO
        lis=[]
        temp=self.head
        
        while temp is not None:
            if temp.value in lis:
                continue
            else:
                lis.append(temp.value)
            
            temp=temp.next

    def hasCycle(self):
        head=self.head
        if not self.head or not self.head.next:
            return False
        slow=self.head
        fast=self.head.next 
        if not slow.next or not fast.next:
            return False
        while slow!=fast:
            if not fast or not fast.next:
                return False
            slow=slow.next
            fast=fast.next.next
        return True
   class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' -> '
            temp_node = temp_node.next
        return result
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        
    def  get(self,index):
        temp=self.head
        if index>self.length-1 or index<0:
            return "list is empty"
        
        for _ in range(index):
            temp=temp.next
        return temp
    def pop_first(self):
        popednode=self.head
        if self.length==0:
            return None
        elif self.length==1:
            self.head=None
            self.tail=None
            
            
        else:
            
            self.head=self.head.next
            popednode.next=None
        self.length-=1
        return popednode
        
        
    def pop(self):
        temp=self.head
        popednode=self.tail
        if self.head==None:
            return None
        elif self.length==1:
            self.head=None
            self.tail=None
            
        else:
            while temp.next != self.tail:
                temp=temp.next
            
            temp.next=None
            self.tail=temp
        self.length-=1 
        return popednode
        
            
            
            
    def remove(self,index):
        if self.head==None:
            return None
        if index ==0:
            
            return self.pop_first()
            
        elif index<0 or index>=self.length:
            return "length of index exceeds"
        elif index==(self.length)-1:
           
            return self.pop()
            
        else:    
            prev=self.get(index-1)
            popednode=prev.next
            prev.next=popednode.next
            popednode.next=None
        self.length-=1
        return popednode
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
    
    def find_middle(self):
        n=self.length%2
        rem=self.length//2
        if n==0:
            return self.get(rem).value
        else:
            return self.get(rem).value
            
    def remove_duplicates(self):
        # TODO
        lis=[]
        temp=self.head
        
        while temp is not None:
            if temp.value in lis:
                continue
            else:
                lis.append(temp.value)
            
            temp=temp.next

    def hasCycle(self):
        head=self.head
        if not self.head or not self.head.next:
            return False
        slow=self.head
        fast=self.head.next 
        if not slow.next or not fast.next:
            return False
        while slow!=fast:
            if not fast or not fast.next:
                return False
            slow=slow.next
            fast=fast.next.next
        return True
    def remove_2(self,n):
        head=self.head
        temp=head
        prev=None
        i=0
        j=0
        
        if not temp or not temp.next:
            return None
        
        while temp:
            j=j+1
            temp=temp.next
        print(j)
        temp=head
        
        while temp is not None:
            
            if int(j-i)==n:
                if n==j:
                    head=head.next
                    return head
                elif n==1:
                    prev.next=None
                    return head
                
                elif prev:
                    prev.next=temp.next
                    temp.next=None
                    return head
            
            print(i)
            i=i+1
            prev=temp
            temp=temp.next
        return head


    #---------------------------------------------------------------------------------------------------------------------
    def removeNthFromEnd(self, head): #two pointer solution 
         # Create a dummy node to handle edge cases
        dummy = ListNode(0)
        dummy.next = head
        fast, slow = dummy, dummy

        # Move the fast pointer n steps ahead
        for _ in range(n):
            fast = fast.next

        # Move both fast and slow pointers until fast reaches the end
        while fast.next:
            fast = fast.next
            slow = slow.next

        # Remove the nth node from the end
        slow.next = slow.next.next


        
       
        
            
    
            
            
      
       
       
            
            
        
n=LinkedList()
for i in range(6):
    n.append(i)
print(n)

n.remove_2(5)
print(n)


