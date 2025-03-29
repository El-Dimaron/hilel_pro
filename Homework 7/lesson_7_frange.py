class frange:
    def __init__(self, start: float, end: float = Ellipsis, step: float = 1):
        self.start = start
        self.step = step
        if end == Ellipsis:
            self.end = start
            self.start = 0
        else:
            self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.step < 0:
            if self.end >= self.start:
                raise StopIteration
            else:
                result = self.start
                self.start += self.step
                return self.__result_check(result, self.step)

        if self.start >= self.end:
            raise StopIteration
        result = self.start
        self.start += self.step
        return self.__result_check(result, self.step)

    def __decimal_num(self, number: float) -> float:
        """Returns the number of digits after the decimal point."""
        return len(str(number).split(".")[1])

    def __result_check(self, result: float, step: float) -> float:
        """Checks if the resulted number is a float.
        If it is, then the function makes sure to return the float with the same number of digits after the decimal
        point as in the entered 'step' number."""
        if not isinstance(result, float):
            return result

        if self.__decimal_num(step) == self.__decimal_num(result):
            return result
        else:
            return round(result, self.__decimal_num(step))
