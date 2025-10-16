import random

class SlidingPuzzle:
    def __init__(self):
        self.goal_state = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 0]
        ]
        self.state = self._scramble()

    def _scramble(self):
        tiles = [i for i in range(9)]
        random.shuffle(tiles)
        return [tiles[i*3:(i+1)*3] for i in range(3)]

    def display(self):
        for row in self.state:
            print(' '.join(str(x) if x != 0 else ' ' for x in row))
        print()

    def find_empty(self):
        for i in range(3):
            for j in range(3):
                if self.state[i][j] == 0:
                    return i, j

    def move(self, direction):
        # Find position of empty space
        i, j = self.find_empty()
        # Reverse movement: move the number in the direction of input
        moves = {
            'w': (i+1, j),  # move tile down
            's': (i-1, j),  # move tile up
            'a': (i, j+1),  # move tile right
            'd': (i, j-1)   # move tile left
        }
        if direction in moves:
            ni, nj = moves[direction]
            if 0 <= ni < 3 and 0 <= nj < 3:
                # Swap number with empty space
                self.state[i][j], self.state[ni][nj] = self.state[ni][nj], self.state[i][j]
                return True
        return False

    def is_solved(self):
        return self.state == self.goal_state

if __name__ == "__main__":
    puzzle = SlidingPuzzle()
    print("Sliding Puzzle Game (3x3)")
    print("Use commands: w, s, a, d to move the NUMBER tile.")
    print("Goal: Arrange numbers 1–8 with empty space at bottom-right.\n")

    while not puzzle.is_solved():
        puzzle.display()
        move = input("Enter move (up: w / down: s / left: a / right: d): ").strip().lower()
        if not puzzle.move(move):
            print("Invalid move. Try again.")
    print("🎉 Congratulations! You solved the puzzle!")
    puzzle.display()
