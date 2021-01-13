class Roman:
    def __init__(self):
        self.nums = {
            1: "I",
            4: "IV",
            5: "V",
            9: "IX",
            10: "X",
            40: "XL",
            50: "L",
            90: "XC",
            100: "C",
            400: "CD",
            500: "D",
            900: "CM",
            1000: "M"
        }

    def roman(self, value):
        if type(value) != int:
            return 'err'
        result = ""
        for val, num in sorted(self.nums.items(), reverse=True):
            while value >= val:
                result += num
                value -= val
        return result
