from sortedcontainers import SortedList

class MyCalendar:

    def __init__(self):
        self.sorted_list = SortedList(key = lambda x : x[1])

    def book(self, start, end):

        pos = self.sorted_list.bisect((start, end))
        if pos == 0:
            if len(self.sorted_list) == 0:
                self.sorted_list.add((start, end))
                return True
            
            x, y = self.sorted_list[0]
            
            if end > x:
                return False
            else:
                self.sorted_list.add((start, end))
                return True
            
            
        x, y = self.sorted_list[pos-1]
        
        if start < y or start < x:
            return False

        if pos == len(self.sorted_list):
            self.sorted_list.add((start, end))
            return True
        x, y = self.sorted_list[pos]

        if x < end:
            return False
        self.sorted_list.add((start, end))
        return True
