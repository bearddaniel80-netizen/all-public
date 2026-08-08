
# uses sliding_window algorythm to match
# a list within a list, same order and sequencing

class Pattern:
    pattern = ()

    def has_match(self, tokens):
        width = len(self.pattern)

        for i in range(len(tokens) - width + 1):
            self.window = tokens[i:i + width]

            if all(
                token.type == expected
                for token, expected in zip(self.window, self.pattern)
            ):
                return True

        return False
