
class TicTacToe:
    def __init__(self):
        self.board = [[" " for i in range(3)] for j in range(3)]
        self.turn = 1
        self.winner = None
        self.player1 = "O"
        self.player2 = "X"
        
    def print_board(self):
        cnt = 0
        for row in self.board:
            print(row[0]+"|"+row[1]+"|"+row[2])
            cnt += 1
            if(cnt<3):
                print("-----")
    
    def check_winner(self):
        for i in range(3):
            if(self.board[i][0] == self.board[i][1] == self.board[i][2] and self.board[i][0] != " "):
                self.winner = self.board[i][0]
            elif(self.board[0][i] == self.board[1][i] == self.board[2][i] and self.board[0][i] != " "):
                self.winner = self.board[0][i]
        if(self.board[0][0] == self.board[1][1] == self.board[2][2] or self.board[0][2] == self.board[1][1] == self.board[2][0]):
            if(self.board[1][1] != " "):
                self.winner = self.board[1][1]
    
    def play_game(self):
        print("Enter move syntax: 0 0\n")
        self.print_board()
        while self.winner == None and self.turn <=9:
            move = input("Enter move:")
            while(len(move) != 3):
                move = input("Try again:")
            move = move.split(" ")
            if(self.turn % 2 != 0):
                if(self.board[int(move[0])][int(move[1])] == " "):
                    self.board[int(move[0])][int(move[1])] = self.player1
                    self.turn += 1
                else:
                    print("\nINVALID MOVE!\n")
            else:
                if(self.board[int(move[0])][int(move[1])] == " "):
                    self.board[int(move[0])][int(move[1])] = self.player2
                    self.turn += 1
                else:
                    print("\nINVALID MOVE!\n")
            self.check_winner()
            self.print_board()
        if(self.winner != None):
            print("\nPLAYER {} WINS!".format(self.winner))
        else:
            print("\nDRAW!")
            

if __name__ == "__main__":
    game = TicTacToe()
    game.play_game()