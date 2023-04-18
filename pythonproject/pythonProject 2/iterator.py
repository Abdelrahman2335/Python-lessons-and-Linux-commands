# lesson16 is also talking about iterator this important point should be clear.

class MyIterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.end:
            value = self.current
            self.current += 1
            return value
        else:
            raise StopIteration

my_iterator = MyIterator(0, 5)
for item in my_iterator:
    print(item)


class MyRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return MyRangeIterator(self)

class MyRangeIterator:
    def __init__(self, range_obj):
        self.current = range_obj.start
        self.range_obj = range_obj

    def __next__(self):
        if self.current >= self.range_obj.end:
            raise StopIteration
        value = self.current
        self.current += 1
        return value

my_range = MyRange(1, 5)
for i in my_range:
    print(i)


