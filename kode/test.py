from brikker import Brikker


hand_1 = ["1","2","3","4","5"]
hand_2 = ["1","2","3","4","5"]
board = ["1","2","3","4","5","6","7","8","9"]
felter = {1: "",2: "",3: "",4: "",5: "",6: "",7: "",8: "",9: ""}
#chose brick
chosenbrick = None
user_input = int(input("which piece?"))#Example "1" -> DrowlanceMaster
if user_input not in range(1, 6): 
            print("Input has to be 1 to 5")
else:
    for piece in range(1, 6):
        if user_input == piece: # tildel de 5 forskellige brikker en værdi fra 1 til 5
            chosenbrick = piece


#chose collum
chosenfelt = None
user_input = int(input("which collum?")) #Example "1" -> collum 1
if user_input not in range(1, 10): 
            print("Input has to be 1 to 9")

for key, felt in felter.items():
    print(user_input == key)
    if user_input == key and felt == "": # vælger et felt og ligge brikken på
        felter[key] = chosenbrick





print(felter)