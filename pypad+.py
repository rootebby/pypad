import time
file_name = input("File Name : ")

with open(file_name,"w",encoding="UTF-8") as file:
	sayı = 1
	while True:
		
		yaz = input("==>>(to exit - 'q') : ")
		if yaz == "q":
			print("Countdown 5 to shutdown !!!")
			time.sleep(4)
			print("Goodbye !!")
			time.sleep(1)
			break

		elif len(yaz) == 0:
			pass

		else:			
			file.write( str(sayı) + ":" + str(yaz) + "\n" )
			sayı += 1
