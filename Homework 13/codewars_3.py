# Link:
# https://www.codewars.com/kata/5c556845d7e0334c74698706/train/python

def fit_in(a, b, m, n):
    return a + b <= max(m, n) and max(a, b) <= min(m, n)
