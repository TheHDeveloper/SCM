import sys
pos = [" " for i in range(0,10)]
pos[5] = "O"

def display_board():
    print(pos[1],"  | ",pos[2],"|",pos[3])
    print("----|----|----")
    print(pos[4],"  | ",pos[5],"|",pos[6])
    print("----|----|----")
    print(pos[7],"  | ",pos[8],"|",pos[9])

def usr_ent():
    pass

def main():
    print("Welcome To Tic-Tac-Toe  Game!!!\n")
    print("Rules Are As Follows: \n1). You Are Playing As a 'X'\n2). There is Already a 'O' Present in the middle\n3). First One to get a 3 in row WINS.\n\n")
    display_board()
main()
