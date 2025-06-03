from typing import Generator, Callable


def custom_map(dictionary: dict, function_1: Callable, function_2: Callable) -> Generator:
    for key, value in dictionary.items():
        yield tuple((function_1(key), function_2(value)))


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


print(list(custom_map(dictionary=test_dict, function_1=func_1, function_2=func_2)))
