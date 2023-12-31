import tkinter as tk
import tkinter.font as font
import time
 
class TicTacToe:
    def __init__(self):
        self.board = [[" " for i in range(3)] for j in range(3)]
        self.turn = 1
        self.winner = None
        self.player1 = "O"
        self.player2 = "X"
        self.winning = []
        
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
                self.winning = [(i,0),(i,1),(i,1)]
            elif(self.board[0][i] == self.board[1][i] == self.board[2][i] and self.board[0][i] != " "):
                self.winner = self.board[0][i]
                self.winning = [(0,i),(1,i),(2,i)]
        if(self.board[0][0] == self.board[1][1] == self.board[2][2] or self.board[0][2] == self.board[1][1] == self.board[2][0]):
            if(self.board[1][1] != " "):
                self.winner = self.board[1][1]
                if(self.board[0][0] == self.board[1][1]):
                    self.winning = [(0,0),(1,1),(2,2)]
                else:
                    self.winning = [(0,2),(1,1),(2,0)]
    
    def terminal_game(self,window):
        window.destroy()
        print("Enter move syntax: 0 0\n")
        self.print_board()
        while self.winner == None and self.turn <=9:
            move = input("Enter move: ")
            while(len(move) != 3):
                move = input("Try again: ")
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
            
    def register_move(self,place,button,window):
        if(self.turn % 2 != 0 and self.board[place[0]][place[1]] == " "):
            self.board[place[0]][place[1]] = self.player1
            button["text"] = self.player1
            self.turn += 1    
        elif(self.board[place[0]][place[1]] == " "):
            self.board[place[0]][place[1]] = self.player2  
            button["text"] = self.player2  
            self.turn += 1
        self.check_winner()
        if(self.winner != None or self.turn == 10):
            for button in window.winfo_children():
                button.configure(state="disabled")
            
            
            
            
    def window_game(self,choose_window):
        choose_window.destroy()
        window = tk.Tk(className=" TicTacToe")
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x_cordinate = int((screen_width/2) - (530/2))
        y_cordinate = int((screen_height/2) - (540/2))
        window.resizable(0,0)
        window.geometry("{}x{}+{}+{}".format(530, 540, x_cordinate, y_cordinate))
        buttonFont = font.Font(size="20",weight="bold")
        b0 = tk.Button(window,height=7,width=10, font=buttonFont, command=lambda: self.register_move((0,0),b0,window))
        b1 = tk.Button(window,height=7,width=10, font=buttonFont, command=lambda: self.register_move((1,0),b1,window))
        b2 = tk.Button(window,height=7,width=10, font=buttonFont, command=lambda: self.register_move((2,0),b2,window))
        b3 = tk.Button(window,height=7,width=10, font=buttonFont, command=lambda: self.register_move((0,1),b3,window))
        b4 = tk.Button(window,height=7,width=10, font=buttonFont, command=lambda: self.register_move((1,1),b4,window))
        b5 = tk.Button(window,height=7,width=10, font=buttonFont, command=lambda: self.register_move((2,1),b5,window))
        b6 = tk.Button(window,height=7,width=10, font=buttonFont, command=lambda: self.register_move((0,2),b6,window))
        b7 = tk.Button(window,height=7,width=10, font=buttonFont, command=lambda: self.register_move((1,2),b7,window))
        b8 = tk.Button(window,height=7,width=10,font=buttonFont, command=lambda: self.register_move((2,2),b8,window))
        
        b0.grid(row=0,column=0)
        b1.grid(row=1,column=0)
        b2.grid(row=2,column=0)
        b3.grid(row=0,column=1)
        b4.grid(row=1,column=1)
        b5.grid(row=2,column=1)
        b6.grid(row=0,column=2)
        b7.grid(row=1,column=2)
        b8.grid(row=2,column=2)
        
        window.mainloop()
       
            
    def play_game(self):
        choose_window = tk.Tk(className=" Choose Window")
        choose_window.geometry("200x110")
        choose_window.resizable(0,0)
        choose_window.eval('tk::PlaceWindow . center')
        txt = tk.Label(text = " Choose Game")
        terminal_button = tk.Button(choose_window,text=" Play in terminal", command=lambda: self.terminal_game(choose_window))
        window_button = tk.Button(choose_window,text=" Play in window", command=lambda: self.window_game(choose_window))
        exit_button = tk.Button(choose_window,text=" Exit", command=lambda: choose_window.destroy())
        txt.pack()
        terminal_button.pack()
        window_button.pack()
        exit_button.pack()
        choose_window.mainloop()
        
            

if __name__ == "__main__":
    game = TicTacToe()
    game.play_game()