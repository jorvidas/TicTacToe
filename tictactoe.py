#board/state
#type
#action
from random import choice, randint
import time

class TicTacToe:
  def __init__(self):
    self.board = [["_","_","_"],
                  ["_","_","_"],
                  [" "," "," "]]
    self.winner = ""
    self.empty_cells = [" ", "_"]
    self.players = ["X","O"]
    self.next_turn = choice(self.players)
    self.X = None
    self.O = None

  def get_player_type(self, symbol):
    player_type = input("Is "+symbol+" a computer or player? ")
    if player_type.lower() == "computer":
      return ComputerChallenger()
    elif player_type == "player":
      return Player()

  def startup_menu(self):
    while not self.X:
      self.X = self.get_player_type("X")
    while not self.O:
      self.O = self.get_player_type("O")

  def clear_board(self):
    '''
    Resets the board to a blank board for a new game.
    '''
    self.board = [["_","_","_"],
                  ["_","_","_"],
                  [" "," "," "]]
    self.winner = ""
    self.next_turn = choice(self.players)


  def check_board(self):
    '''
    Checks the board to see if there is a winner or full board. Adjusts the member winner if so.
    '''
    checks = [[[0,0], [0,1], [0,2]],
              [[1,0], [1,1], [1,2]],
              [[2,0], [2,1], [2,2]],
              [[0,0], [1,0], [2,0]],
              [[0,1], [1,1], [2,1]],
              [[0,2], [1,2], [2,2]],
              [[0,0], [1,1], [2,2]],
              [[0,2], [1,1], [2,0]]]
    #loop over each and check for winner
    for check in checks:
      one = self.board[check[0][0]][check[0][1]]
      two = self.board[check[1][0]][check[1][1]]
      three = self.board[check[2][0]][check[2][1]]

      if one == two == three not in self.empty_cells:
        self.winner = self.next_turn
        return

    #check that there is an empty cell
    empty_cell = False
    for row in range(3):
      for column in range(3):
        if self.board[row][column] in self.empty_cells:
          return

    self.winner = "tie"

  #add to the board, team 1 is x, 2 is o, position 0 - 8 right to left, top to bottom
  def add_to_board(self, position):
    col = position % 3
    row = position // 3
    assert self.board[row][col] in self.empty_cells
    self.board[row][col] = self.next_turn

  def print_board(self):
    horiz_div = "_{}_|_{}_|_{}_"
    bottom =    " {} | {} | {} "
    for i in [0,1]:
      print(horiz_div.format(self.board[i][0], self.board[i][1], self.board[i][2]))
    print(bottom.format(self.board[2][0], self.board[2][1], self.board[2][2]))

  def change_turn(self):
    '''
    Changes next turn to the other player.
    '''
    assert self.next_turn in self.players
    if self.next_turn == self.players[0]:
      self.next_turn = self.players[1]
    else:
      self.next_turn = self.players[0]

  def get_move_from_player(self):
    position = -1
    while position not in list(range(9)):
      position = input(self.next_turn + " it is your turn, please input the position you wish to place your mark (0-8): ")
      if position.lower() == "exit":
        return "exit"
      try:
        position = int(position)
      except:
        pass
    return position

  def get_move_from_computer(self, computer):
    print("Computer's turn:")
    time.sleep(1)
    return computer.get_move(self.board)

  def get_move(self):
    next_computer = getattr(self, self.next_turn)
    if isinstance(next_computer, ComputerChallenger):
      return self.get_move_from_computer(next_computer)
    else:
      return self.get_move_from_player()

  def play_game(self):
    '''
    The actual game. Runs once.
    '''
    play = True

    self.startup_menu()
    while play:
      while not self.winner:
        self.print_board()
        position = self.get_move()
        if position == "exit":
          return
        try:
          self.add_to_board(position)
          self.check_board()
          if not self.winner:
            self.change_turn()
        except:
          print("\n---That spot is already taken.---")
        
      self.print_board()
      if self.winner == "tie":
        print("X and O have tied!")
      else:
        print(self.next_turn+" has won!")

      response = input("Would you like to play again?")
      if response.lower() != "yes" and response.lower() != "y":
        play = False
      else:
        self.clear_board()

class ComputerChallenger():
  def __init__(self):
    self.random_percentage = 1

  def get_move(self, board):
    return randint(0,8)

class Player():
  def __init__(self):
    pass

if __name__ == "__main__":

  game = TicTacToe()
  game.play_game()