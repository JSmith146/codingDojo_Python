
class Underscore:
    def map(self, iterable, callback):
        for x in range(len(iterable)):
            iterable[x] = callback(iterable[x])
            return iterable

    def find(self, iterable, callback):
        for val in iterable:
            if callback(val):
                return val
    
    def filter(self, iterable, callback):
        new_arr = []
        for val in iterable:
            if callback(val):
                new_arr.append(val)
        return new_arr
    
    def reject(self, iterable, callback):
        new_arr = []
        for val in iterable:
            if not callback(val):
                new_arr.append(val)
        return new_arr
        
        # your code
# you just created a library with 4 methods!
# let's create an instance of our class
_ = Underscore() # yes we are setting our instance to a variable that is an underscore
evens = _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
# should return [2, 4, 6] after you finish implementing the code above