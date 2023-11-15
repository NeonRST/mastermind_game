import random


class Mastermind:
    def __init__(self, rows, rn, dup):
        self.rows = rows
        self.rn = rn
        self.dup = dup
        temp_ans = ""
        while len(temp_ans) < self.rows:
            answer = random.randint(1, self.rn)
            if self.dup:
                if str(answer) not in temp_ans:
                    temp_ans += str(answer)
            else:
                temp_ans += str(answer)
        self.temp_ans = temp_ans
    
    def playing(self):
        guess = input(f"input {self.rows} numbers: ")
        output = ""
        for i in range(self.rows):
            if guess[i] == self.temp_ans[i]:
                output += "0"
            elif guess[i] in self.temp_ans:
                output += "X"
            else:
                output += "_"
        print(output)
        if guess == self.temp_ans:
            print("you win good job")
            return False
        else:
            return True

