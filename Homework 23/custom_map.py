class map:
    def __init__(self, dictionary, function_1, function_2):
        self.i_dictionary = iter(dictionary.items())
        self.function_1 = function_1
        self.function_2 = function_2

    def __iter__(self):
        return self

    def __next__(self):
        key, value = next(self.i_dictionary)
        return tuple((self.function_1(key), self.function_2(value)))


########
# Test #
########

test_dict = {
    "alpha": 1,
    "bravo": 2,
    "charlie": 3,
    "delta": 4,
    "echo": 5,
}


def func_1(string: str):
    binary_list = [bin(ord(symbol))[2:] for symbol in string]
    return "".join(binary_list)


def func_2(n):
    return n ** 2


print(list(map(dictionary=test_dict, function_1=func_1, function_2=func_2)))
