import functools
from collections import OrderedDict
import requests
from random import choice


def lfu_cache(max_limit=3):
    def internal(f):
        @functools.wraps(f)
        def deco(*args, **kwargs):
            cache_key = (args, tuple(kwargs.items()))

            if cache_key in deco._cache:
                deco._cache_frq[cache_key] += 1
                return deco._cache[cache_key]

            result = f(*args, **kwargs)

            if len(deco._cache) >= max_limit:
                least_used_list = list(sorted(deco._cache_frq.items(), key=lambda x: x[1], reverse=True))
                least_used_key = least_used_list[-1][0]

                deco._cache.pop(least_used_key)
                deco._cache_frq.pop(least_used_key)

            deco._cache[cache_key] = result
            # in order to keep track of a frequency, each key will be assigned a frequency counter value
            deco._cache_frq[cache_key] = 1

            return result

        deco._cache = OrderedDict()
        deco._cache_frq = OrderedDict()

        return deco

    return internal


@lfu_cache
def fetch_url(url, first_n=100):
    """Fetch a given url"""
    res = requests.get(url)
    return res.content[:first_n] if first_n else res.content


# Testing ground
if __name__ == "__main__":
    url_1 = "https://stackoverflow.com/questions/45114985/how-to-create-an-ordereddict-in-python"
    url_2 = "https://docs.python.org/3/library/collections.html"
    url_3 = "https://www.w3schools.com/python/python_dictionaries_methods.asp"
    url_4 = "https://docs.python.org/3/library/collections.html#collections.OrderedDict"

    for x in range(10):
        url = choice((url_1, url_2, url_3, url_4))
        fetch_url(url)
