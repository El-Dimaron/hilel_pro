# Link:
# https://leetcode.com/problems/bulls-and-cows/submissions/1623959096/


class Solution:

    @staticmethod
    def getHint(secret: str, guess: str) -> str:
        bulls = {}
        secret_dict = {}
        guess_dict = {}
        cows = 0

        for i in range(len(guess)):
            if guess[i] == secret[i]:
                bulls[guess[i]] = bulls.get(guess[i], 0) + 1

            if secret[i] not in secret_dict:
                secret_dict[secret[i]] = secret.count(secret[i])

            if guess[i] not in guess_dict:
                guess_dict[guess[i]] = guess.count(guess[i])

        for key, value in secret_dict.items():
            if key in guess_dict:
                cows += min(value, guess_dict[key])

        intersection_set = secret_dict.keys() & guess_dict.keys()
        intersection_num = 0
        for item in intersection_set:
            intersection_num += bulls.get(item, 0)

        cows -= intersection_num
        bulls = sum(bulls.values())

        return f"{bulls}A{cows}B"
