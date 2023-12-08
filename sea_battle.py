import random
import os

class Game:
    def __init__(self):
        self.board = [["." for _ in range(7)] for _ in range(7)]
        self.player_board = [["." for _ in range(7)] for _ in range(7)]
        self.ship_coords = []
        self.generate_ship_coords()
        self.place_ships()

    def generate_ship_coords(self):
        for _ in range(4):
            self.ship_coords.append(random.randint(0, 6))
        for _ in range(3):
            self.ship_coords.append(random.randint(0, 13))
        for _ in range(2):
            self.ship_coords.append(random.randint(0, 20))
        for _ in range(1):
            self.ship_coords.append(random.randint(0, 27))

    def place_ships(self):
        for i in range(len(self.ship_coords)):
            for j in range(7):
                if (self.ship_coords[i] - i >= 0 and
                        self.ship_coords[i] + i < 6 * 7 and
                        self.board[self.ship_coords[i] // 7][self.ship_coords[i] % 7] == "."):
                    for k in range(-i, i + 1):
                        self.board[self.ship_coords[i] // 7 + k // 7][self.ship_coords[i] % 7 + k % 7] = "S"
                    break

    def display_board(self):
        for row in self.board:
            print(" ".join(row))

    def start_game(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            self.display_board()
            try:
                guess = input("Enter your guess (e.g., 'A2'): ")
                guess = guess.upper()
                if len(guess) != 3 or guess[0] not in "ABCDEFG" or guess[1] not in "1234567" or guess[2] not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                    raise ValueError
                x, y = ord(guess[0]) - ord("A"), int(guess[1]) - 1
                if self.player_board[x][y] != ".":
                    raise ValueError
                self.player_board[x][y] = "X"
                if self.board[x][y] == "S":
                    print("Hit!")
                else:
                    print("Miss.")
                if self.check_win():
                    print("Congratulations, " + self.player_name + "! You've sunk all the ships.")
                    break
            except ValueError:
                print("Invalid input. Please try again.")

    def check_win(self):
        for row in self.player_board:
            if "." in row:
                return False
        return True

game = Game()
game.start_game()