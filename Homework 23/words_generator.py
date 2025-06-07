from itertools import islice
from typing import Generator

import nltk
from nltk.corpus import words

nltk.download('words', quiet=True)


def word_generator(n: int) -> Generator:
    def _generator():
        unique_words = set(word for word in words.words())
        yield from islice(unique_words, n)

    max_value = 10_000
    if n > max_value:
        raise ValueError(f"The number of generated words must be less than {max_value}")
    if n < 0:
        raise ValueError("The number of generated words must be more than 0")
    return _generator()
