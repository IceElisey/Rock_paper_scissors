print("подбрось монетку")
monetka = input("что выпало? если орёл - напиши о, а если решка то напиши - р ")
if monetka == "о" or monetka == "О":
    print("вы выиграли")
elif monetka == "р" or monetka == "Р":
    print("вы проиграли")
else:
    print("к сожелению, я не понимаю что вы написали, напишите корректно")
print("брось кубик")
kubik = int(input("напиши, что тебе выпало (1, 2, 3, 4, 5 или 6 "))
if kubik == "1" or kubik == "2" or kubik == "3":
    print("ты выиграл")
elif kubik == "4" or kubik == "5" or kubik == "6":
    print("ты проиграл")
else:
    print("напиши конкретней") 


