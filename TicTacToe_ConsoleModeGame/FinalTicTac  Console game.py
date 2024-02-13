import random
position1,position2,position3,position4,position5,position6,position7,position8,position9=1,2,3,4,5,6,7,8,9
playstatus = "Y"
while playstatus == "Y" or playstatus == "y":
    playingMode = input("Welcome to The tic Tak toe Game \n\n Please enter \"M\" for Multiplayer or \"S\" for single player: ")
    while playingMode != "s" and playingMode != "S" and playingMode != "m" and playingMode != "M":
        playingMode = input("You enter a wrong key Please enter \"M\" for Multiplayer or \"S\" for single player: ")
    compuToss_status, Win_status ,player1toss_status =0,0,0
    if playingMode == "s" or playingMode == "S":
        player1name= input("Enter player1 name please:")
        print("frist we have to made a toss, so If a Input on your screen is 1 then player 1 win the toss or if 2 came then AI win the toss")
        toss = random.randint(1,2)       #doing toss
        print(toss)
        if toss == 1:
            print(player1name, "Won the toss")
            compuToss_status = 0
            player1symbol = input("Choice your symbol [\"X\"] or [\"O\"]:") #choice the symbol which you like
            while player1symbol != "X" and player1symbol != "x" and player1symbol != "o"  and player1symbol != "O":
                player1symbol = input("Choice a valid symbol form this: [\"X\"] or [\"O\"]")
            if (player1symbol == "X") or (player1symbol == "x"):compu_symbol = "O"
        else:
            compuToss_status = 1
            print("AI Won the toss")
            compu_symbol = "X"
            player1symbol = "O"
        print(player1name, "symbol is:",player1symbol)
        print("Computer symbol is:",compu_symbol)
    else:
        player1name= input("Enter player1 name please:")
        player2name= input("Enter player2 name please:")
        print("frist we have to made a toss, so If a Input on your screen is 1 then player 1 win the toss or if 2 came then player two win the toss")
        toss = random.randint(1,2)       #doing toss
        print(toss)
        if toss == 1:
            print(player1name, "Won the toss")
            compuToss_status = 0
            player1toss_status =1
            player1symbol = input("Choice your symbol [\"X\"] or [\"O\"]:") #choice the symbol which you like
            while player1symbol != "X" or player1symbol != "x" or player1symbol != "o"  or player1symbol != "O":
                player1symbol = input("Choice a valid symbol form this: [\"X\"] or [\"O\"]")
            if (player1symbol == "X") or (player1symbol == "x"):player2symbol = "O"
        else:
            print(player2name, "Won the toss")
            compuToss_status = 0
            player1toss_status = 0
            player2symbol = input("Choice your symbol [\"X\"] or [\"O\"]:") #choice the symbol which you like
            while player2symbol != "X" and player2symbol != "x" and player2symbol != "o"  and player2symbol != "O":
                player2symbol = input("Choice a valid symbol form this: [\"X\"] or [\"O\"]")
            if (player2symbol == "X") or (player2symbol == "x"):player1symbol = "O"
        print(player1name, "symbol is:",player1symbol)
        print(player2name, "symbol is:",player2symbol)
    print("\t\t\t\t",position1,"|",position2,"|",position3,"\n\t\t\t\t","----------","\n\t\t\t\t",position4,"|",position5,"|",position6,"\n\t\t\t\t","----------","\n\t\t\t\t",position7,"|",position8,"|",position9)
    for i in range(0,9):
        if compuToss_status ==1 and (playingMode == "s" or playingMode == "S"):
            compuToss_status = 0
            print("It is computer trun")
            if (((position7==compu_symbol and position4 == compu_symbol) or (position9==compu_symbol and position5 == compu_symbol) or (position3==compu_symbol and position2 == compu_symbol)) and type(position1) == int): Input = 1
            elif (((position1==compu_symbol and position2 == compu_symbol) or (position9==compu_symbol and position6 == compu_symbol) or (position7==compu_symbol and position5 == compu_symbol))and  type(position3) == int):Input = 3
            elif (((position1==compu_symbol and position4 == compu_symbol) or (position9==compu_symbol and position8 == compu_symbol) or (position5==compu_symbol and position3 == compu_symbol)) and  type(position7) == int):Input = 7
            elif (((position1==compu_symbol and position5 == compu_symbol) or (position7==compu_symbol and position8 == compu_symbol) or (position3==compu_symbol and position6 == compu_symbol)) and  type(position9) == int):Input = 9
            elif (((position1==compu_symbol and position3 == compu_symbol) or (position8==compu_symbol and position5 == compu_symbol)) and type(position2) == int):Input = 2
            elif (((position1==compu_symbol and position7 == compu_symbol) or (position6==compu_symbol and position5 == compu_symbol)) and type(position4)== int):Input = 4
            elif (position9==compu_symbol and position3 == compu_symbol or position4==compu_symbol and position5 == compu_symbol)and type(position6)==int:Input = 6
            elif (position7==compu_symbol and position9 == compu_symbol or position5==compu_symbol and position2 == compu_symbol) and type(position8)== int:Input = 8
            elif (position8==compu_symbol and position2 == compu_symbol or position4==compu_symbol and position6 == compu_symbol or position3==compu_symbol and position7 == compu_symbol or position1==compu_symbol and position9 == compu_symbol)and  type(position5) == int:Input = 5
            elif (position7==player1symbol and position4 == player1symbol or position9==player1symbol and position5 == player1symbol or position3==player1symbol and position2 == player1symbol)and type(position1) == int: Input = 1
            elif (position1==player1symbol and position2 == player1symbol or position9==player1symbol and position6 == player1symbol or position7==player1symbol and position5 == player1symbol) and type(position3) == int:Input = 3
            elif (position1==player1symbol and position4 == player1symbol or position9==player1symbol and position8 == player1symbol or position5==player1symbol and position3 == player1symbol) and type(position7) == int:Input = 7
            elif (position1==player1symbol and position5 == player1symbol or position7==player1symbol and position8 == player1symbol or position3==player1symbol and position6 == player1symbol) and type(position9) == int:Input = 9
            elif ((position1==player1symbol and position3 == player1symbol)or (position8==player1symbol and position5 == player1symbol)) and type(position2) == int:Input = 2
            elif (position1==player1symbol and position7 == player1symbol or position6==player1symbol and position5 == player1symbol) and type(position4) == int:Input = 4
            elif (position9 == player1symbol and position3 == player1symbol or position4==player1symbol and position5 == player1symbol) and type(position6) == int:Input = 6
            elif (position7==player1symbol and position9 == player1symbol or position5==player1symbol and position2 == player1symbol) and type(position8) == int:Input = 8
            elif (position8==player1symbol and position2 == player1symbol or position4==player1symbol and position6 == player1symbol or position3==player1symbol and position7 == player1symbol or position1==player1symbol and position9 == player1symbol) and type(position5) == int:Input = 5
            elif type(position5) == int:Input = 5
            elif ((position2== compu_symbol and position4==compu_symbol) or (position3== compu_symbol and position4==compu_symbol) or (position2== compu_symbol and position7==compu_symbol)) and type(position1)==int:Input = 1
            elif ((position8== compu_symbol and position6==compu_symbol) or (position3== compu_symbol and position8==compu_symbol) or (position6== compu_symbol and position7==compu_symbol)) and  type(position9)== int:Input = 9
            elif ((position8== compu_symbol and position4==compu_symbol) or (position8== compu_symbol and position1==compu_symbol) or (position4== compu_symbol and position9==compu_symbol)) and type(position7)== int:Input = 7   
            elif ((position2== compu_symbol and position6==compu_symbol) or (position6== compu_symbol and position1==compu_symbol) or (position2== compu_symbol and position9==compu_symbol)) and type(position3)==int:Input = 3
            elif ((position5== compu_symbol and position7==compu_symbol) and type(position1)==int and type(position4) == int) or ((position5== compu_symbol and position3==compu_symbol) and type(position1)==int and type(position2) == int):Input = 1
            elif ((position5== compu_symbol and position1==compu_symbol) and type(position7)==int and type(position4) == int) or ((position5== compu_symbol and position9==compu_symbol) and type(position8)==int and type(position7) == int):Input = 7   
            elif ((position5== compu_symbol and position1==compu_symbol) and type(position2)==int and type(position3) == int) or ((position5== compu_symbol and position9==compu_symbol) and type(position6)==int and type(position3) == int):Input = 3
            elif ((position5== compu_symbol and position7==compu_symbol) and type(position8)==int and type(position9) == int) or ((position5== compu_symbol and position3==compu_symbol) and type(position6)==int and type(position9) == int):Input = 9     
            elif (position2 == position4 == player1symbol or player1symbol == position4 == position3 or player1symbol == position2 == position7)and type(position1) == int:Input = 1
            elif (position8 == position4 == player1symbol or player1symbol == position4 == position9 or player1symbol == position1 == position8)and type(position7) == int:Input = 7
            elif (position2 == position6 == player1symbol or player1symbol == position6 == position1 or player1symbol == position2 == position9)and type(position3) == int:Input = 3
            elif (position8 == position6 == player1symbol or player1symbol == position6 == position7 or player1symbol == position8 == position3) and type(position9) == int:Input = 9
            elif ((position1 == position9 == player1symbol) or (position3  ==player1symbol ==position7)) and type(position8) == int:Input = 8
            elif (i == 1) and type(position5) != int:Input = 7
            elif (i == 2) and Input == 1:Input = 9
            elif (i == 2) and Input == 3:Input = 7
            elif (i == 2) and Input == 7:Input = 3
            elif (i == 2) and Input == 9:Input = 1
            elif (i == 2) and Input % 2 == 0:Input = 1
            elif type(position1) == int:Input = 1
            elif type(position3) == int:Input = 3
            elif type(position9) == int:Input = 9
            elif type(position4) == int:Input = 4
            elif type(position2) == int:Input = 2
            elif type(position6) == int:Input = 6
            elif type(position8) == int:Input = 8
            else:
                print("Something Wrong with program")
            
            if Input == 1:position1 = compu_symbol
            elif Input == 2:position2 = compu_symbol
            elif Input == 3:position3 = compu_symbol
            elif Input == 4:position4 = compu_symbol
            elif Input == 5:position5 = compu_symbol
            elif Input == 6:position6 = compu_symbol
            elif Input == 7:position7 = compu_symbol
            elif Input == 8:position8 = compu_symbol
            elif Input == 9:position9 = compu_symbol
            print("\t\t\t\t",position1,"|",position2,"|",position3,"\n\t\t\t\t","----------","\n\t\t\t\t",position4,"|",position5,"|",position6,"\n\t\t\t\t","----------","\n\t\t\t\t",position7,"|",position8,"|",position9)
            if position1==position2==position3 or position4==position5==position6 or position6==position3==position9 or position1==position4==position7 or position2==position5==position8 or position3==position5==position7 or position1==position5==position9 or position9==position8==position7:
                print("AI Wins the game")
                win_status = 1
                break
        elif  player1toss_status == 0 and (playingMode == "M" or playingMode == "m"):
            player1toss_status = 1
            validInput = 0
            while validInput == 0:
                print(player2name,"It is your Turns: choice your Input")
                Input = eval(input())
                if Input == 1 and type(position1) == int:validInput = 1
                elif Input == 2 and type(position2) == int:validInput = 1
                elif Input == 3 and type(position3) == int:validInput = 1
                elif Input == 4 and type(position4) == int:validInput = 1
                elif Input == 5 and type(position5) == int:validInput = 1
                elif Input == 6 and type(position6) == int:validInput = 1
                elif Input == 7 and type(position7) == int:validInput = 1
                elif Input == 8 and type(position8) == int:validInput = 1
                elif Input == 9 and type(position9) == int:validInput = 1
                else:print("Invalid Entry Try Again")    
            if Input == 1:position1 = player2symbol
            elif Input == 2: position2 = player2symbol
            elif Input == 3:position3 = player2symbol
            elif Input == 4:position4 = player2symbol
            elif Input == 5:position5 = player2symbol
            elif Input == 6:position6 = player2symbol
            elif Input == 7:position7 = player2symbol
            elif Input == 8:position8 = player2symbol
            elif Input == 9:position9 = player2symbol
            print("\t\t\t\t",position1,"|",position2,"|",position3,"\n\t\t\t\t","----------","\n\t\t\t\t",position4,"|",position5,"|",position6,"\n\t\t\t\t","----------","\n\t\t\t\t",position7,"|",position8,"|",position9)
            if position1==position2==position3 or position4==position5==position6 or position7==position8==position9 or position1==position4==position7 or position2==position5==position8 or position3==position6==position9 or position1==position5==position9 or position9==position8==position7 :
                print(player2name, "Win The Game")
                win_status = 1        
                break
        else:
            compuToss_status = 1
            player1toss_status = 0
            validInput = 0
            while validInput == 0:
                print(player1name,"It is your Turns: choice your Input")
                Input = eval(input())
                if Input == 1 and type(position1) == int:validInput = 1
                elif Input == 2 and type(position2) == int:validInput = 1
                elif Input == 3 and type(position3) == int:validInput = 1
                elif Input == 4 and type(position4) == int:validInput = 1
                elif Input == 5 and type(position5) == int:validInput = 1
                elif Input == 6 and type(position6) == int:validInput = 1
                elif Input == 7 and type(position7) == int:validInput = 1
                elif Input == 8 and type(position8) == int:validInput = 1
                elif Input == 9 and type(position9) == int:validInput = 1
                else:print("Invalid Entry Try Again")
            if Input == 1:position1 = player1symbol
            elif Input == 2: position2 = player1symbol
            elif Input == 3:position3 = player1symbol
            elif Input == 4:position4 = player1symbol
            elif Input == 5:position5 = player1symbol
            elif Input == 6:position6 = player1symbol
            elif Input == 7:position7 = player1symbol
            elif Input == 8:position8 = player1symbol
            elif Input == 9:position9 = player1symbol
            print("\t\t\t\t",position1,"|",position2,"|",position3,"\n\t\t\t\t","----------","\n\t\t\t\t",position4,"|",position5,"|",position6,"\n\t\t\t\t","----------","\n\t\t\t\t",position7,"|",position8,"|",position9)
            if position1==position2==position3 or position4==position5==position6 or position7==position8==position9 or position1==position4==position7 or position2==position5==position8 or position3==position6==position9 or position1==position5==position9 or position9==position8==position7 :
                print("You can never win",player1name, "\nAI still Wins the game")
                win_status = 1        
                break
    if win_status != 1:
        print("Match is tie")
    playstatus = input("If you want to play again press \"Y\" or if you want to exit the game press any another key")
