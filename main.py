import random
import time 


count = 0
for number in range(10):
    time.sleep(1)
    player = int(input("выбери ход: 1-камень 2-ножницы 3-бумага "))
    if player == 1:
        print("ваш ход камень")
    elif player == 2:
        print("ваш ход ножницы")
    elif player == 3:
        print("ваш ход бумага") 
    time.sleep(1)
    computer = random.randint(1, 3)
    if computer == 1:
        print("ход компьютера -- камень")
    elif computer == 2:
        print("ход компьютера -- ножницы")
    elif computer == 3:
        print("ход компьтера -- бумага")
    if player == 1 and computer == 2:
        count += 1
        print("ты выиграл, поздравляю!")
    elif player == computer:
        print("ничья!")
    elif player == 3 and computer == 2:
        print("ты проиграл, но не расстраивайся, выиграешь в следующий раз! :) ") 
    elif player == 2 and computer == 1:
        print("ты проиграл, но не расстраивайся, выиграешь в следующий раз! :) ")
    elif player == 3 and computer == 1:
        count += 1
        print("ты выиграл, молодец! ")
    if player == 1 and computer == 3:
        print("ты проиграл, но не расстраивайся, выиграешь в следующий раз! :)")
    elif player == 2 and computer == 3:
        count += 1
        print("ты выиграл, отлично! ")
print("ты выиграл --",count, "раз")
    
       

  
          

