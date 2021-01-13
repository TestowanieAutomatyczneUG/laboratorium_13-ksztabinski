class FizzBuzz:
    def fizzybuzzy(self, num):
        if type(num) != int:
            return 'err'
        elif num % 3 == 0 and num % 5 == 0:
            return 'FizzBuzz'
        elif num % 3 == 0:
            return 'Fizz'
        elif num % 5 == 0:
            return 'Buzz'
        else:
            return 'ani fizz ani buzz'