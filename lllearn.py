class Node:   # Represent individual member in the linked list 
    def __init__(self,data = None , next =None):
        self.data = data 
        self.next = next  #pointer to next element

class Linkedlist:
    def __init__(self):
        self.head = None  #points to head of the linkedlist

   
    def insert_at_begining(self,data):
        node = Node(data , self.head)    
        self.head = node

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return

        itr = self.head  #iterator
        llstr = ''

        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next

        print(llstr)      

    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data , None)
            return

        itr = self.head
        
        while itr.next:
            itr = itr.next 
        
        itr.next = Node(data,None)  

    def insert_values(self, data_list):
        self.head = None 
        for data in data_list:
            self.insert_at_end(data)       

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next

        return count     

    def remove_at(self , index):
        if index<0 or index >= self.get_length() :
            raise Exception("Invalid index")

        if index == 0 :
            self.head = self.head.next 
            return 

        count = 0 

        itr = self.head 
        while itr:
            if count == index-1:
                itr.next = itr.next.next
                break 

            itr =itr.next   
            count += 1 
                   
    def insert_at(self , index , data):
        if index<0 or index >= self.get_length() :
            raise Exception("Invalid index")

        if index == 0:
            self.insert_at_begining(data)
            return

        count = 0
        itr = self.head 
        while itr:
            if count == index - 1 :
                node = Node(data , itr.next)
                itr.next = node 
                break 

            itr = itr.next
            count += 1    

    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            return

        if self.head.data==data_after:
            self.head.next = Node(data_to_insert,self.head.next)
            return

        itr = self.head
        while itr:
            if itr.data == data_after:
                itr.next = Node(data_to_insert, itr.next)
                break

            itr = itr.next


    def contains(self,data):
        if self.head is None:
             return

        checker = self.head
        while checker is not None:
            if checker.data == data :
                return True 

            checker = checker.next

        return False        


    def remove_by_value(self, data):
        if self.head is None:
            return

        if ll.contains(data) == False :
            print("No such item exist in list")    

        if self.head.data == data:
            self.head = self.head.next
            return    

        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            
            itr = itr.next








if __name__ == '__main__':
    # ll = Linkedlist()
    # ll.insert_at_begining(9)
    # ll.insert_at_begining(90)
    # ll.insert_at_end(190)
    # ll.insert_at_end(150)
    # ll.insert_at_end(160)
    # ll.insert_values(["banana","mango","grapes","oranges"])
    # ll.print()     
    # ll.remove_at(2)
    # ll.print()
    # ll.insert_at(0,"chiku")
    # ll.print()
    # ll.insert_at(2,"kiwi")
    # ll.print()     
    # print("Length of list:",ll.get_length())
    ll = Linkedlist()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print()
    ll.insert_after_value("mango","apple") # insert apple after mango
    ll.print()
    ll.remove_by_value("orange") # remove orange from linked list
    ll.print()
    ll.remove_by_value("figs")
    ll.print()
    ll.remove_by_value("banana")
    ll.print()
    ll.remove_by_value("mango")
    ll.print()
    ll.remove_by_value("apple")
    ll.print()
    ll.remove_by_value("grapes")
    ll.print()



