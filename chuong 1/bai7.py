class Date:
    def __init__(self, day=1, month=1, year=2000):
        self.day = day
        self.month = month
        self.year = year

    def display(self):
        print(f"{self.day:02d}/{self.month:02d}/{self.year}")

    def next(self):
        day_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        #kt năm nhuận
        if (self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0):
            day_in_month[1] = 29
        
        self.day += 1
        if self.day > day_in_month[self.month -1]:
            self.day = 1
            self.month += 1

            if self.month > 12:
                self.month = 1
                self.year += 1

date = Date(27, 2, 2005)
date.display()
date.next()
date.display()


