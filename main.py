import smtplib
import os
import time

def clear():
	if os.name == "nt":
		os.system("cls")

	else:
		os.system("clear")


def gmailSpam(email, password, victim, content):
	try:
		server = smtplib.SMTP('smtp.gmail.com', 587)
		server.ehlo()
		server.starttls()
		server.login(email, password)
		clear()
		print("ALL SET. TYPE 1 TO CONTINUE: ")
		a= input()

		if a == "1":
			while True:
				try:
					server.sendmail(email, victim, content)

				except KeyboardInterrupt as e:
					server.close()

	except Exception as e:
		print(e)
		print("ERROR OCCURED")
		input()

def yahooSpam(email, password, victim, content):
	try:
		server = smtplib.SMTP('smtp.yahoo.com', 587)
		server.ehlo()
		server.starttls()
		server.login(email, password)
		clear()
		print("ALL SET. TYPE 1 TO CONTINUE: ")
		a= input()

		if a == "1":
			while True:
				try:
					server.sendmail(email, victim, content)

				except KeyboardInterrupt as e:
					server.close()

	except Exception as e:
		print(e)
		print("ERROR OCCURED")
		input()


def home():
	clear()
	with open("home.log", "r") as e:
		home = e.read()
		print(home)
		choice = input()

		if choice == "1":
			with open("get_ap.log", "r") as f:
				f= f.read()
				print(f)
				email = input("\n| EMAIL: ")
				password= input("\n\n| PASSWORD: ")
				vemail = input("\n\n| VICTIM'S EMAIL: ")
				content = input("\n\n| CONTENT: ")


				if vemail.endswith("gmail.com"):
					gmailSpam(email, password, vemail, content)

				else:
					print("[ERROR] INVALID EMAIL!")
					time.sleep(1)
					home()
			

		elif choice == "2":
			with open("get_ap.log", "r") as f:
				f= f.load()
				print(f)
				email = input("\n| EMAIL: ")
				password= input("\n\n| PASSWORD: ")
				vemail = input("\n\n| VICTIM'S EMAIL: ")
				content = input("\n\n| CONTENT: ")

				if vemail.endswith("yahoo.com"):
					yahooSpam(email, password, vemail, content)

				else:
					print("[ERROR] INVALID EMAIL!")
					time.sleep(1)
					home()
			

		else:
			print("\n[ERROR] This script only works with gmail or yahoo.")
			time.sleep(1)
			home()
home()
