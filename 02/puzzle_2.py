import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

class RPSGame():
    """Class represents Rock Paper Scissors game."""

    def __init__(self, score = 0) -> None:
        self.elf_move = 0
        self.player_move = 0
        self.score = score

    def set_game(self, strategy: list) -> None:
        """Set game of Rock Paper Scissors based on line in input file.

        Args:
            strategy (list): List with two single letter string elements representing player and elf move.
        """        
        match strategy[0]:
            case "A": # Rock
                self.elf_move = 1
            case "B": # Paper
                self.elf_move = 2
            case "C": # Scissors
                self.elf_move = 3

        match strategy[1]:
            case "X": # Lose
                self.player_move = (self.elf_move-2) % 3 + 1
            case "Y": # Draw
                self.player_move = self.elf_move
            case "Z": # Win
                self.player_move = (self.elf_move) % 3 + 1

        self.score = self.player_move + \
            + (self.player_move     == self.elf_move)*3 + \
            + (self.player_move - 1 == self.elf_move)*6 + \
            + (self.player_move + 2 == self.elf_move)*6
        
        print(self)

    def __str__(self) -> str:
        emoji = ["✊", "✋", "✌️"]
        return f"🧝 plays {emoji[self.elf_move-1]}, 👱 play {emoji[self.player_move-1]}! Game score is {self.score}."

    def __radd__(self, other):
        return other + self.score

list_of_games = []

if __name__ == "__main__":
    with open(os.path.join(__location__,"input.txt")) as file:
        lines = [line for line in (l.strip() for l in file)]
        i = 0
        for input_line in lines:
            game = RPSGame()
            game.set_game(input_line.split())
            list_of_games.append(game)

print(sum(list_of_games))