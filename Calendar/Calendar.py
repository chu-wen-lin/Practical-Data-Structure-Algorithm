from sortedcontainers import SortedList
import bisect


class Calendar:
    def __init__(self):
        self.calendar_list = SortedList()  # initialize a sorted list using default constructor

    def book(self, start, end):
        # if calendar_list is empty:
        if not self.calendar_list:
            self.calendar_list.add((start, end))  # insert start & end
            return True  # booking event is allowed

        # if calendar_list is not empty:
        bisect_index = self.calendar_list.bisect_left(
            (start, end))  # get index(where to insert, without destroying order)

        if bisect_index == 0:  # start <= self.calendar_list[0][0]
            if end <= self.calendar_list[0][0]:  # both start & end are smaller than self.calendar_list[0][0]
                self.calendar_list.add((start, end))  # add current event tuple into calender_list
                return True
            return False  # end is larger than self.calendar_list[0][0] --> overlapping --> return False

        elif bisect_index == len(self.calendar_list):  # start >= self.calendar_list[-1][0]
            if start >= self.calendar_list[-1][1]:  # start >= e in last tuple
                self.calendar_list.add((start, end))  # add current event tuple into calender_list
                return True
            return False  # start is less than self.calendar_list[-1][1] --> overlapping --> return False

        else:  # self.calender_list[0][0] < current start < self.calender_list[-1][0]
            left_tuple = self.calendar_list[bisect_index - 1]
            right_tuple = self.calendar_list[bisect_index]

            if start >= left_tuple[1] and end <= right_tuple[0]:  # current tuple is in unbooked interval
                self.calendar_list.add((start, end))
                return True

            return False
