

class NumberAsWord:
    numbers_dict_0_to_19 = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', \
            6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', \
            11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', \
            15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
    numbers_dict_10s = {20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety'}
    value: str
    
    def __init__(self, number: int) -> None:
        self.value = self._number_to_str(number)

    def _number_to_str(self, number: int) -> str:
        if (number >= 0) and (number <= 19):
            return self.numbers_dict_0_to_19[number]
        elif (number >= 20) and (number <= 99):
            remainder = number % 10
            if remainder == 0:
                return self.numbers_dict_10s[number]
            else:
                tens = number - remainder
                return f'{self.numbers_dict_10s[tens]} {self.numbers_dict_0_to_19[remainder]}'
        else:
            raise Exception('not a number')
