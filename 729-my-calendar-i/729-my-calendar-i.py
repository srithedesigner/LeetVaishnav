from sortedcontainers import SortedList
class MyCalendar(object):

    def __init__(self):
        self.sorted_list = SortedList(key = lambda x : x[0])

    def book(self, start, end):

        pos = self.sorted_list.bisect((start, end))

        if pos < len(self.sorted_list):

            x, y = self.sorted_list[pos]

            if x < end:
                return False

        if pos > 0:
            x, y = self.sorted_list[pos-1]

            if y > start:
                return False

        self.sorted_list.add((start, end))
        return True
