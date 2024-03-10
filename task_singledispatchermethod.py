from functools import singledispatchmethod

class Processor:

    @singledispatchmethod
    @classmethod
    def process(cls, value):
        # if isinstance(value, int | float ):
        #     return value*2
        # elif isinstance(value, str):
        #     return value.upper()
        # elif isinstance(value, list):
        #     value.sort()
        #     return value
        # else:
        raise TypeError('No format')
    @process.register(int)
    @classmethod
    def from_int(cls, val):
        return val * 2

    @process.register(list)
    @classmethod
    def from_list(cls, val:list):
        return val.sort()

print(Processor.process(1))
# print(Processor.process('asfasf'))
# print(Processor.process(4.5))
print(Processor.process([6,4,3,2,1]))
