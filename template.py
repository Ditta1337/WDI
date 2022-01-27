
if __name__ == "__main__":
    
    class collection():
        def __init__(self, new_value = None):
            self.value = new_value
            self.next = None

        def add(self, new_value):
            if self.next == None:
                self.next = collection(new_value)
                return
            self.next.add(new_value)
        
        def push_front(self, new_value):
            item = collection(new_value)
            item.next = self.next
            self.next = item

        def add_in_order(self, new_value):
            if self.next == None:
                self.next = collection(new_value)
                return True
            
            item = self
            while item.next != None:
                val = item.next.value
                if new_value == val:
                    return False
                
                if new_value == min(val, new_value):
                    tmp = item.next
                    item.next = collection(new_value)
                    item.next.next = tmp
                    return True

                item = item.next
            item.next = collection(new_value)
            return True

        def get_len(self):
            if self.value == None and self.next == None:
                return 0

            if self.value == None:
                return self.next.get_len()

            if self.next == None:
                return 1

            return self.next.get_len() + 1

        def print(self):
            if self.next != None:
                val = self.next
                while val.next != None:
                    print(val.value, end=", ")
                    val = val.next

                print(val.value)

    class collection2():
        def __init__(self, new_value = None):
            self.value = new_value
            self.next = None
            self.prev = None

        def append(self, new_value):
            item = self
            while item.next != None:
                item = item.next

            item.next = collection2(new_value)
            item.next.prev = item
        
        def print(self):
            if self.next != None:
                val = self.next
                while val.next != None:
                    print(val.value, end=", ")
                    val = val.next

                print(val.value)

        def print_backwards(self):
            if self.next != None:
                val = self.next
                while val.next != None:
                    val = val.next
                while val.prev != None:
                    print(val.value, end=", ")
                    val = val.prev

                print(val.prev) 

    cla2 = collection2()
    cla2.append(3)
    cla2.append(5)
    cla2.append(7)
    cla2.append(11)
    cla2.print()


