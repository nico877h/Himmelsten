from brikker import Brikker


hand_1 = ["1","2","3","4","5"]
hand_2 = ["1","2","3","4","5"]
board = ["1","2","3","4","5","6","7","8","9"]
#chose brick
chosenbrick = None
user_input = input("which piece?") #Example "1" -> DrowlanceMaster
for piece in hand:
    if user_input == piece: # tildel de 5 forskellige brikker en værdi fra 1 til 5
        chosenbrick = piece
        hand.remove(piece)
    else:
        if input not in list.hand: 
            print("Input has to be 1 to 5")

#chose collum
chosenfelt = None
user_input = input("which collum?") #Example "1" -> collum 1
for felt in board:
    if user_input == felt and felt == empty: # vælger et felt og ligge brikken på
        chosenfelt = felt
    else:
        if input not in list.board: 
            print("Input has to be 1 to 5")


print(input)
