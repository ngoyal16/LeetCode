class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone_number_char = {
            "0": [],
            "1": [],
            "2": [
                "a", "b", "c"
            ],
            "3": [
                "d", "e", "f"
            ],
            "4": [
                "g", "h", "i"
            ],
            "5": [
                "j", "k", "l"
            ],
            "6": [
                "m", "n", "o"
            ],
            "7": [
                "p", "q", "r", "s"
            ],
            "8": [
                "t", "u", "v"
            ],
            "9": [
                "w", "x", "y", "z"
            ]
        }

        
        append_with = lambda output, char_d: list(map(lambda temp_ch: temp_ch + char_d, output))

        output = []
        for digit in digits:
            if len(output) == 0:
                output = phone_number_char[digit]
            else:
                temp = []

                for char_d in phone_number_char[digit]:
                    temp = temp + append_with(output, char_d)
                output = temp

        return output
