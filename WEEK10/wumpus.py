import random

class WumpusWorld:
    def __init__(self, size=4):
        self.size = size
        self.agent_pos = (0, 0)
        self.wumpus_pos = self.place_wumpus()
        self.gold_pos = self.place_gold()
        self.pits = self.place_pits()
        self.has_gold = False
        self.game_over = False

    def place_wumpus(self):
        return (random.randint(0, self.size - 1), random.randint(0, self.size - 1))

    def place_gold(self):
        while True:
            pos = (random.randint(0, self.size - 1), random.randint(0, self.size - 1))
            if pos != self.agent_pos and pos != self.wumpus_pos:
                return pos

    def place_pits(self):
        pits = set()
        while len(pits) < 3:
            pos = (random.randint(0, self.size - 1), random.randint(0, self.size - 1))
            if pos != self.agent_pos and pos != self.wumpus_pos:
                pits.add(pos)
        return pits

    def perceive(self):
        stench = self.wumpus_pos in self.get_adjacent(self.agent_pos)
        breeze = any(pit in self.get_adjacent(self.agent_pos) for pit in self.pits)
        return stench, breeze

    def get_adjacent(self, pos):
        x, y = pos
        adjacent = []
        if x > 0:
            adjacent.append((x - 1, y))
        if x < self.size - 1:
            adjacent.append((x + 1, y))
        if y > 0:
            adjacent.append((x, y - 1))
        if y < self.size - 1:
            adjacent.append((x, y + 1))
        return adjacent

    def move_agent(self, direction):
        if self.game_over:
            print("Game over!")
            return

        x, y = self.agent_pos
        if direction == 'up' and x > 0:
            self.agent_pos = (x - 1, y)
        elif direction == 'down' and x < self.size - 1:
            self.agent_pos = (x + 1, y)
        elif direction == 'left' and y > 0:
            self.agent_pos = (x, y - 1)
        elif direction == 'right' and y < self.size - 1:
            self.agent_pos = (x, y + 1)
        else:
            print("Invalid move!")
            return

        self.check_status()

    def check_status(self):
        if self.agent_pos == self.wumpus_pos:
            print("You were eaten by the Wumpus!")
            self.game_over = True
        elif self.agent_pos in self.pits:
            print("You fell into a pit!")
            self.game_over = True
        elif self.agent_pos == self.gold_pos:
            print("You found the gold!")
            self.has_gold = True
            self.game_over = True

    def play(self):
        print("Welcome to Wumpus World!")
        while not self.game_over:
            stench, breeze = self.perceive()
            print(f"Agent postn: {self.agent_pos}")
            print(f"Perceptions - Stench: {stench}, Breeze: {breeze}")
            move = input("Enter your move (up, down, left, right): ").strip().lower()
            self.move_agent(move)

if __name__ == "__main__":
    game = WumpusWorld()
    game.play()
