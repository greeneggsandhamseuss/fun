board = ["0", "1", "2",
         "3", "4", "5",
         "6", "7", "8",]               

checklist = [
    [0,1,2],
    [3,4,5],
    [6,7,8],
    [0,3,6],
    [1,4,7],
    [2,5,8],
    [0,4,8],
    [6,4,2],
]   

def DrawBoard():
    print('\n')
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print('\n')


def is_winner(a:str, b:str, c:str) -> str:  
    if a == b == c:
        return a 
    return "_"

def check_for_winner(): 
    for set in checklist:
        result = is_winner(board[set[0]],board[set[1]],board[set[2]])
        if result in ["X","O"]: 
            return result
    return "_"
                
def main():
    current_player = "X"
    print('\n')
    print("Welcome to Tic-Tac-Toe!")

    while True:
        DrawBoard()
        print(f"Player {current_player}'s turn.")

        move = input("Choose a position (0-8):   ").strip()

        if not move.isdigit() or int(move) < 0 or int(move) > 8:
            print("Invalid input! Please choose position from 0-8.")
            continue 

        pos = int(move)

        if board[pos] in ["X", "O"]:
            print("That spot is already taken! Please try another.")
            continue

        board[pos] = current_player

        winner = check_for_winner()

        if winner in ["X","O"]:
            DrawBoard()
            print(f"Player {winner} is the winner!")
            break

        elif all(position in ["X", "O"] for position in board):
            DrawBoard()
            print("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"

main()



    

  





     






    
    




