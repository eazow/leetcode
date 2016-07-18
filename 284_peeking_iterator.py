class Iterator(object):
    def __init__(self, nums):
        """
        Initializes an iterator object to the beginning of a list.
        :type nums: List[int]
        """
        self.nums = nums
        self.top = 0
        self.count = len(nums)

    def hasNext(self):
        """
        Returns true if the iteration has more elements.
        :rtype: bool
        """
        return self.top < self.count

    def next(self):
        """
        Returns the next element in the iteration.
        :rtype: int
        """
        num = self.nums[self.top]
        self.top += 1
        return num

class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.value = None
        if self.iterator.hasNext():
            self.value = self.iterator.next()

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.value

    def next(self):
        """
        :rtype: int
        """
        value = self.value
        if self.iterator.hasNext():
            self.value = self.iterator.next()
        else:
            self.value = None
        return value

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.value!=None

nums = [1,2]
iter = PeekingIterator(Iterator(nums))
assert(iter.hasNext()==True)
assert(iter.peek() == 1)
assert(iter.next()==1)
assert(iter.hasNext()==True)
assert(iter.peek() == 2)
assert(iter.peek() == 2)
assert(iter.next() == 2)
assert(iter.hasNext() == False)

