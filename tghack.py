import random
pzhsp=1
pzhsn=1
theme="no"
print("Добро пожаловать в TGHACK\nСписок доступных комманд:\n[.spam] - установить спамблок на аккаунт\n[.info] - узнать информацию аккаунта\n[.del] - удалить аккаунт")
print("Разработано CaT (Code and Technologies)")
while True:
	act=input("Введите нужную команду: .")
	if act=="spam":
		theme="sp"
		if theme=="sp":
			input("Введите юзернейм аккаунта: @")
			for i in range (10):
				print("Подача жалоб на аккаунт ("+str(pzhsp)+"/10)")
				pzhsp+=1
			print("Жалобы на аккаунт поданы, в ближайшее время на аккаунт будет наложен спамблок")
			pzhsp=1
			theme="no"
	if act=="info":
		theme="in"
		if theme=="in":
			input("Введите юзернейм аккаунта: @")
			print("Данные аккаунта:\nUsername: @username\nID:1234567890\nName: Telegram\nOld: 18\nPhone number: +7 777 777 77 77")
			theme="no"
	if act=="del":
		theme="de"
		if theme=="de":
			input("Введите юзернейм аккаунта: @")
			for i in range (234):
				print("Подача жалоб на аккаунт ("+str(pzhsn)+"/234)")
				pzhsn+=1
			print("Жалобы на аккаунт поданы, в ближайшее время аккаунт будет удален")
			pzhsn=1
			theme="no"
