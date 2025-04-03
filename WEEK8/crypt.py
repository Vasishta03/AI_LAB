#crypt arithmetic problem

class Puzzle:
    def __init__(self,puzzle):
        self.puzzle = puzzle
        self.assignement = {}
        self.rem_letters = list(set(puzzle[0]+puzzle[1]+puzzle[2]))
        for letter in self.rem_letters:
            self.assignement[letter] = None
        self.rem_letters

    def subs_word(self,assignment,word):
        return int("".join(str(assignment[letter]) for letter in word))
    
    def check_soln(self,assignment):
        first = self.subs_word(assignment,self.puzzle[0])
        second = self.subs_word(assignment,self.puzzle[1])
        result = self.subs_word(assignment,self.puzzle[2])
        return first + second == result
    
    def is_valid_assign(self,assignment,word):
        return all(assignment[letter] is not None for letter in word)
    
    def backtrack(self,assignment,rem_letters):
        if not rem_letters:
            if self.check_soln(assignment):
                print('Found Solution')
                print(assignment)
                exit()
            return
        curr_letter = rem_letters.pop()
        for digit in range(10):
            if digit not in assignment.values():
                assignment[curr_letter] = digit
                if self.is_valid_assign(assignment,curr_letter):
                    self.backtrack(assignment.copy(),rem_letters.copy())
                assignment[curr_letter] = None
        rem_letters.append(curr_letter)

    def solve_cryptic(self):
        self.backtrack(self.assignement,self.rem_letters)
        print("No Solution!")


# Input
puz = Puzzle(input("Enter Puzzle: ").split(","))
puz.solve_cryptic()

#Enter Puzzle: CROSS,ROADS,DANGER
#Found Solution
#{'D': 1, 'N': 8, 'E': 4, 'A': 5, 'S': 3, 'C': 9, 'O': 2, 'G': 7, 'R': 6}

#Enter Puzzle: DONALD,GERALD,ROBERT
#Found Solution
#{'E': 9, 'A': 4, 'T': 0, 'D': 5, 'L': 8, 'N': 6, 'R': 7, 'G': 1, 'B': 3, 'O': 2}

#Enter Puzzle: MIT,MANIPAL,MITMAHE
#No Solution!

#Enter Puzzle: SEND,MORE,MONEY
#Found Solution
#{'Y': 2, 'N': 6, 'D': 7, 'S': 9, 'R': 8, 'M': 1, 'E': 5, 'O': 0}

#Enter Puzzle: COCA,COLA,OASIS
#Found Solution
#{'C': 8, 'O': 1, 'A': 6, 'S': 2, 'I': 9, 'L': 0}
