import random


class Mastermind:
    def __init__(self, rows, rn, dup=False):
        self.rows = rows
        self.rn = rn
        self.dup = dup
        self.temp_ans = ""
        self.game_history = []

    def menu(self):
        temp_ans = ""
        while len(temp_ans) < self.rows:
            answer = random.randint(1, self.rn)
            if self.dup:
                temp_ans += str(answer)
            else:
                if str(answer) not in temp_ans:
                    temp_ans += str(answer)
        self.temp_ans = temp_ans
        print(f"Playing Mastermind with {self.rn} positions and {self.rows} positions")
        print(f"duplicates set as {self.dup}")

    def playing(self):
        guess = input(f"input {self.rows} numbers: ")

        if guess == "hint":
            print("Hint:")
            print(f"one of the answers is {self.temp_ans[random.randint(1, (self.rows - 1))]}")
        output = ""
        for i in range(self.rows):
            if guess[i] == self.temp_ans[i]:
                output += "0"
            elif guess[i] in self.temp_ans:
                output += "X"
            else:
                output += "_"
        for i in range(len(output)):
            print(f"[{output[i]}]", end=" ")
        self.game_history.append([guess, output])
        print()
        if guess == self.temp_ans:
            print("you win good job")
            print()
            return False
        else:
            return True

