# Link:
# https://www.codewars.com/kata/57a5b0dfcf1fa526bb000118/train/python

def distinct(seq):
    new_seq = []
    for num in seq:
        if num not in new_seq:
            new_seq.append(num)
    return new_seq
