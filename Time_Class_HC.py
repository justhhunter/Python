# Hunter Copening
# 6/11/2022

# Section 10.4.2 Time Class

# Updated and changed to only do the total seconds in a day

# timewithproperties.py
# class with read write properties

class Time:


    def __init__(self, second=0):
        print('Initialize total seconds attribute')

        
        self.second = second #0-59

    

    @property
    def second(self):
        print('return the total seconds')
        return self._total_seconds

    @second.setter
    def second(self, second):
        print('set the second')
        if not (0 <= second < 86400):
            raise ValueError(f'Second ({second}) must be 0-59')

        self._total_seconds = second


    def set_time(self, second=0):
        print('set value for second')
        self.second = second


    def __repr__(self):
        print('Return time string for repr()')
        return (f'second={self.second})')

    def __str__(self):
        print("""Print Time in total seconds format.""")
        return(f'Total seconds since midnight ' f'{self.second}')

# 86400 seconds in a day
time1 = Time(80000)

print(time1)
