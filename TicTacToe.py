import tkinter as tk
import tkinter.font as font
import copy
 
class TicTacToe:
    def __init__(self):
        self.board = [[" " for i in range(3)] for j in range(3)]
        self.turn = 1
        self.player1 = "O"
        self.player2 = "X"
        self.versusPC = False
        self.winning = []
        
    def vsPC(self,window):
        self.versusPC = not self.versusPC
    
    def num_to_pos(self,num):
        pos = [(0,0),(1,0),(2,0),(0,1),(1,1),(2,1),(0,2),(1,2),(2,2)]
        return pos[num]
    
    def check_player(self,state):
        cnt = 1
        for i in range(len(state)):
            for j in range(len(state[i])):
                if state[i][j] != " ":
                    cnt += 1
        if(cnt%2==0):
            return self.player2
        return self.player1
            
    def print_board(self):
        cnt = 0
        for row in self.board:
            print(row[0]+"|"+row[1]+"|"+row[2])
            cnt += 1
            if(cnt<3):
                print("-----")
                
    def possible_actions(self,state):
        actions = []
        for i in range(len(state)):
            for j in range(len(state[i])):
                temp =  [[" " for i in range(3)] for j in range(3)]
                if(state[i][j] == " "):
                    temp[i][j] = self.check_player(state)
                    actions.append(temp)
        return actions
                    
    def applied_action(self,state,action):
        temp_board = copy.deepcopy(state)
        for i in range(len(action)):
            for j in range(len(action[i])):
                if(action[i][j] != " "):
                    temp_board[i][j] = action[i][j]
        return temp_board
    
    def get_value(self,state):
        if(self.check_winner(state) == self.player1):
            return -1
        elif(self.check_winner(state) == self.player2):
            return 1
        return 0
    
    def max_player(self,state):
        #jos uvijek ne odabire optimalan move!!!!!
        if(self.check_winner(state) != ""):
            return self.get_value(state)
        v = float('-inf')
        for action in self.possible_actions(state):
            v = max(v,self.min_player(self.applied_action(state,action)))
        return v
            
    def min_player(self,state):
        if(self.check_winner(state) != ""):
            return self.get_value(state)
        v = float('inf')
        for action in self.possible_actions(state):
            v = min(v,self.max_player(self.applied_action(state,action)))
        return v
    
    def check_winner(self,state,window=None):
        winner = ""
        for i in range(3):
            if(state[i][0] == state[i][1] == state[i][2] and state[i][0] != " "):
                winner = state[i][0]
                self.winning = [(i,0),(i,1),(i,2)]
            elif(state[0][i] == state[1][i] == state[2][i] and state[0][i] != " "):
                winner = state[0][i]
                self.winning = [(0,i),(1,i),(2,i)]
        if(state[0][0] == state[1][1] == state[2][2] or state[0][2] == state[1][1] == state[2][0]):
            if(state[1][1] != " "):
                winner = state[1][1]
                if(state[0][0] == state[1][1] == state[2][2]):
                    self.winning = [(0,0),(1,1),(2,2)]
                else:
                    self.winning = [(0,2),(1,1),(2,0)]
                    
        if((winner != "" or self.turn >= 9) and window !=  None):
            for button in window.winfo_children():
                grid_info = button.grid_info()
                if((grid_info["row"],grid_info["column"]) in self.winning):
                    button["fg"] = "green"
                else:
                    button["state"] = "disabled"
        return winner
            
    
    def terminal_game(self,window):
        window.destroy()
        print("Enter move syntax: 0 0\n")
        self.print_board()
        while self.check_winner(self.board) == "" and self.turn <=9:
            if(self.versusPC != False):
                if(self.turn%2 == 0):
                    possible_states = []
                    for action in self.possible_actions(self.board):
                        possible_states.append(self.applied_action(self.board,action))
                    all_choices = []
                    for state in possible_states:
                        all_choices.append(self.max_player(state))
                    best_choice = all_choices.index(max(all_choices))
                    self.board = possible_states[best_choice]
                    self.turn += 1
                    print("")
                else:
                    move = input("Enter move: ")
                    while(len(move) != 3):
                        move = input("Try again: ")
                    move = move.split(" ")
                    if(self.board[int(move[0])][int(move[1])] == " "):
                        self.board[int(move[0])][int(move[1])] = self.player1
                        self.turn += 1
                    else:
                        print("\nINVALID MOVE!\n")
            else:          
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
            self.print_board()  
        if(self.check_winner(self.board) != ""):
            print("\nPLAYER {} WINS!".format(self.check_winner(self.board)))
        else:
            print("\nDRAW!")
            
    def register_move(self,place,button,window):
        if(self.versusPC == True):
            self.board[place[0]][place[1]] = self.player1
            button["text"] = self.player1
            self.turn += 1  
            self.check_winner(self.board,window)
            possible_states = []
            for action in self.possible_actions(self.board):
                possible_states.append(self.applied_action(self.board,action))
            all_choices = []
            for state in possible_states:
                all_choices.append(self.max_player(state))
            best_choice = all_choices.index(max(all_choices))
            self.board = possible_states[best_choice]
            self.turn += 1
            for i in range(9):
                pos = self.num_to_pos(i)
                window.winfo_children()[i]["text"] = self.board[pos[0]][pos[1]]
        else:
            if(self.turn % 2 != 0 and self.board[place[0]][place[1]] == " "):
                self.board[place[0]][place[1]] = self.player1
                button["text"] = self.player1
                self.turn += 1    
            elif(self.board[place[0]][place[1]] == " "):
                self.board[place[0]][place[1]] = self.player2  
                button["text"] = self.player2  
                self.turn += 1
        
        self.check_winner(self.board,window)
        
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
       
            
    def play_game(self,window = None):
        choose_window = tk.Tk(className=" Choose Window")
        choose_window.geometry("200x140")
        choose_window.resizable(0,0)
        choose_window.eval('tk::PlaceWindow . center')
        txt = tk.Label(text = " Choose Game")
        terminal_button = tk.Button(choose_window,text=" Play in terminal", command=lambda: self.terminal_game(choose_window))
        window_button = tk.Button(choose_window,text=" Play in window", command=lambda: self.window_game(choose_window))
        vs_PC_button = tk.Checkbutton(choose_window,text=" Play vs PC", command=lambda: self.vsPC(choose_window))
        exit_button = tk.Button(choose_window,text=" Exit", command=lambda: choose_window.destroy())
        txt.pack()
        terminal_button.pack()
        window_button.pack()
        vs_PC_button.pack()
        exit_button.pack()
        choose_window.mainloop()
        
            

if __name__ == "__main__":
    game = TicTacToe()
    game.play_game()