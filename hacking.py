import random
print ("Чтобы установить Hacking, пропишите команду .download")
dl=input()
df=1
thm="no"
ans=""
pn=1
ha=""
if dl==".download":
	for i in range (14):
		print ("Установка файлов Hacking... "+"("+str(df)+"/14)")
		df+=1
	print ("Hacking установлен")
	print ("ДОБРО ПОЖАЛОВАТЬ В HACKING")
	print ("Список доступных комманд:\n.passwords - скопировать пароли с устройств поблизости\n.hack - взлом аккаунта\n.rat - удаление RAT-вирусов\n.def - защита от кибератаки")
	print ("Разработано CaT (Code and Technologies)")
	while True:
		ans=input()
		if ans==".passwords":
			thm="pw"
			if thm=="pw":
				print ("Все пароли от устройств в радиусе "+str(random.randint(50,100))+" метров были скопированы в файл passwords"+str(pn)+".txt")
				pn+=1
				thm="no"
		if ans==".hack":
			thm="hk"
			if thm=="hk":
				print("Укажите тип аккаунта: mc - Minecraft-аккаунт rbx - Roblox-аккаунт tg - Telegram-аккаунт gm - GMail-почта")
				ha=input()
				if ha=="mc":
					input("Введите ник игрока, которого хотите взломать: ")
					print ("Пароль от Minecraft-аккаунта был скопирован в файл passwords"+str(pn)+".txt")
					pn+=1
					thm="no"
				if ha=="rbx":
					input("Введите ник игрока, которого хотите взломать: ")
					print ("Пароль от Roblox-аккаунта был скопирован в файл passwords"+str(pn)+".txt")
					pn+=1
					thm="no"
				if ha=="tg":
					input("Введите юзернейм пользователя, которого хотите взломать: ")
					print ("Пароль от Telegram-аккаунта был скопирован в файл passwords"+str(pn)+".txt")
					pn+=1
					thm="no"
				if ha=="gm":
					input("Введите почту пользователя, которого хотите взломать: ")
					print ("Пароль от GMail-почты был скопирован в файл passwords"+str(pn)+".txt")
					pn+=1
					thm="no"
		if ans==".rat":
			thm="rt"
			if thm=="rt":
				print ("Все RAT-вирусы были удалены с этого устройства")
				thm="no"
		if ans==".def":
			thm="df"
			if thm=="df":
				print ("Ваш IP-адрес: защищен\nВаша эелектронная почта: защищена\nВаши личные данные: защищены\nДанные от ваших аккаунтов: защищены")
				thm="no"
else:
	print ("Неизвестная команда")
