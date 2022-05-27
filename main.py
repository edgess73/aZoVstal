import random as r
import time as t
import datetime as dt

print("AZOVSTAL")
input("Press Enter to enter Azovstal")
#Idea by kvartirant
#Simplification by Edges
#
pname = input("Кликуха: ")
pname.lower()
php = int(100)
patk = r.randint(1,10)
pxp = int(0)
plvl = 1
pkills = 0
pie = "Пирожок"
motherland = "Землица Русская"
colddog = "Собачий корм"
empty = "Пусто"
inv1 = empty
inv2 = empty
inv3 = motherland
print("Удачи, " + pname)
print("Вход в Азовстали")
pig_names = ["Рядовой", "Азовец", "Десантник", "Пограничник", "Ивангай", "Школьник зигомётчик"]
while php > 0:
	pig_now = r.choice(pig_names)
	if pig_now == "Рядовой":
		pighp = 10
		pigatk = 3
		pigxpdrop = 3
	elif pig_now == "Азовец":
		pighp = 15
		pigatk = 5
		pigxpdrop = 10
	elif pig_now == "Десантник":
		pighp = 20
		pigatk = 7
		pigxpdrop = 15
	elif pig_now == "Пограничник":
		pighp = 20
		pigatk = 8
		pigxpdrop = 17
	elif pig_now == "Ивангай":
		pighp = 3
		pigatk = 5
		pigxpdrop = 1
	elif pig_now == "Школьник зигомётчик":
		pighp = 2
		pigatk = 1
		pigxpdrop = 0
	else:
		print("WTF so bugy")
	while pighp > 0:
		print("1. Атака.")
		print("2. Предмет.")
		print("3. Информация.")
		choice = input("➥ ")
		if choice == "1":
			pighp = pighp - patk
			php = php - pigatk
			php = str(php)
			print("Жизни: " + php)
			php = int(php)
			pighp = str(pighp)
			print("Жизни свиньи: " + pighp)
			pighp = int(pighp)
		elif choice == "2":
			print("Инветарь:")
			print("1. " + inv1)
			print("2. " + inv2)
			print("3. " + inv3)
			invchoice = input("➥ ")
			if invchoice == "1" and inv1 == pie:
				php = php + 10
				inv1 = empty
				print("10 жизней востановлено")
				print(" ")
			elif invchoice == "1" and inv1 == colddog:
				php = php + 3
				inv1 = empty
				print("3 жизни востановлено")
				print(" ")
			elif invchoice == "2" and inv2 == pie:
				php = php + 10
				inv2 = empty
				print("10 жизней востановлено")
				print(" ")
			elif invchoice == "2" and inv2 == colddog:
				php = php + 3
				inv2 = empty
				print("3 жизни востановлено")
				print(" ")
			elif invchoice == "3":
				php = php + 6
				inv3 = empty
				print("Русская земля поможет! + 6 жизней")
				print(" ")
			if invchoice == "3" and inv3 == pie:
				php = php + 10
				inv3 = empty
				print("10 жизней востановлено")
				print(" ")
			elif invchoice == "3" and inv3 == colddog:
				php = php + 3
				inv3 = empty
				print("3 жизней восстановлено")
				print(" ")
		elif choice == "3":
			pighp = str(pighp)
			pigatk = str(pigatk)
			patk = str(patk)
			pxp = str(pxp)
			php = str(php)
			plvl = str(plvl)
			pkills = str(pkills)
			print("Жизней свиньи: " + pighp)
			print("Атака свиньи: "+ pigatk)
			print("Имя свиньи: " + pig_now)
			print("Ваше имя: " + pname)
			print("Ваша атака: " + patk)
			print("Ваш опыт: " + pxp)
			print("Ваш уровень: " + plvl)
			print("Ваши жизни: " + php)
			print("Убийств: " + pkills)
			print("Инвентарь:")
			print("1. " + inv1)
			print("2. " + inv2)
			print("3. " + inv3)
			print(" ")
			pighp = int(pighp)
			pigatk = int(pigatk)
			patk = int(patk)
			pxp = int(pxp)
			php = int(php)
			plvl = int(plvl)
			pkills = int(pkills)
		else:
			print("Четвёртого не дано")
	pigxpdrop = str(pigxpdrop)
	print(pig_now + " побеждён. + " + pigxpdrop + " опыта")
	pkills = pkills + 1
	pigxpdrop = int(pigxpdrop)
	print("Случайное событие!")
	print("Согласиться? (да/нет)")
	richoice = input("➥ ")
	richoice.lower()
	if richoice == "да":
		rivents = ["eda", "smert", "ranenie"]	
		rivent = r.choice(rivents)
		rfoods = [colddog, pie]
		rfood = r.choice(rfoods)
		if rivent == "eda":
			print("Вот это везение! Вы нашли " + rfood)
			print("В какой слот добавить (Если нет места, то предмет будет заменён): ")
			rinvchoice = input("➥ ")
			if rinvchoice == "1":
				inv1 = rfood
				print(" ")
			elif rinvchoice == "2":
				inv2 = rfood
				print(" ")
			elif rinvchoice == "3":
				inv3 = rfood
			else:
				print("Предмет пропущен")
		elif rivent == "smert":
			print("Вы напоролись на капкан, но вы чудом выжили.")
			print("Вы согласны? (да/нет)")
			ivchoice = input("➥ ")
			ivchoice = ivchoice.lower()
			if ivchoice == "да":
				print("Повезёт в следующий раз ¯\_(ツ)_/¯")
				php = 1
			else:
				print("Чудес не бывает, подумали вы и добили себя")
				php = 0
		elif rivent == "ranenie":
			randatk = r.randint(1,100)
			randatk = str(randatk)
			print("Вы споткнулись и потеряли " + randatk + " жизней")
			randatk = int(randatk)
		else:
			print("WTF so bugy")
	else:
		print("Ивент был пропущен")
print("Игра окончена!")
print("Статистика сохранена в gostats.txt")
patk = str(patk)
pxp = str(pxp)
plvl = str(plvl)
pkills = str(pkills)
f = open('gostats.txt', 'a+')
f.write(t.ctime(t.time()) + "game \n")
f.write(pname + "stats: \n")
f.write("Killed by " + pig_now + " or by random ivent\n")
f.write("Atk: " + patk)
f.write("\nXP: " + pxp)
f.write("\nLVL: " + plvl)
f.write("\nKills: " + pkills)
f.write("\nInventory: ")
f.write("\n1. " + inv1)
f.write("\n2. " + inv2)
f.write("\n3. " + inv3)
f.close()