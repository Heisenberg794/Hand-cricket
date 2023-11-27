print("""                   <~~~ HAND CRICKET ~~>""")
print("""â—Do not use zero for toss and ingameâ—""")
import random
from random import randint
import sys
while True:
	odd_even = input("odd or even ---> ")
	toss = int(input("enter a number for toss ---> "))
	if toss <= 6:
		comp_toss = (random.randint(1,6))
		print("my number for toss is ---> ",comp_toss)
		addition_toss = toss + comp_toss
		if odd_even == "even":
			if addition_toss % 2 == 0:
				print("you won the toss")
		elif odd_even == "odd":
			if addition_toss % 2 != 0:
				print("you won the toss")
		if odd_even == "even":
			if addition_toss % 2 != 0:
				print("I won the toss")
		elif odd_even == "odd":
			if addition_toss % 2 == 0:
				print("I won the toss")	
		if odd_even == "even":
			if addition_toss % 2 == 0:
				bat_bowl = input("you choose batting or bowling ---> ")
				if bat_bowl =="batting":
					t = 0
					u = 0
					while True:
						batting_run =int(input("enter the batting run between 1-6  "))
						comp_run = (random.randint(1,6))
						print("my no.is ",comp_run)
						t += batting_run
						if batting_run == comp_run:
							print("you are out!!! and your score is",t)
							print("now its my turn")
							while True:
								comp_batting_run = int(random.randint(1,6))
								bowling_run = int(input("enter your bowling run b/w 1-6  "))
								print("my batting run is  ",comp_batting_run)
								u += comp_batting_run
								if u > t:
									print("i won the game and my score is",u)
									sys.exit("the game is over")
								if bowling_run == comp_batting_run:
									if t < u:
										print("i won the game and my score is ",u)
										sys.exit("the game is over")
									if t > u:
										print("you won the game and my score is ",u)
										sys.exit("the game is over")									
						else:	
							pass
				if bat_bowl =="bowling":
					t = 0
					u = 0
					while True:
						bowling_run = int(input("enter your bowling run --->  "))
						comp_batting_run = (random.randint(1,6))
						print("my batting run is ---> ",comp_batting_run)
						t += comp_batting_run
						if comp_batting_run == bowling_run:
							print("i am out and my score is",t)
							print("now its your turn")
							while True:
								batting_run = int(input("enter your batting run ---> "))
								comp_bowling_run = (random.randint(1,6))
								print("my bowling run is ---> ",comp_bowling_run)
								u += batting_run
								if comp_bowling_run == batting_run:
									if t > u:
										print("i won the game and my score is",t)
										sys.exit("GAME OVER")
									if u > t:
										print("you won the game and your score is",u)
										sys.exit("GAME OVER")
								if u > t:
									print("you won the game and your score is",u)
									sys.exit("GAME OVER")
						else:
							continue
		elif odd_even == "odd":
			if addition_toss % 2 != 0:
				bat_bowl = input("you choose batting or bowling ---> ")
				if bat_bowl =="batting":
					t = 0
					u = 0
					while True:
						batting_run =int(input("enter the batting run between 1-6  "))
						comp_run = (random.randint(1,6))
						print("my no.is ",comp_run)
						t += batting_run
						if batting_run == comp_run:
							print("you are out!!! and your score is",t)
							print("now its my turn")
							while True:
								comp_batting_run = int(random.randint(1,6))
								bowling_run = int(input("enter your bowling run b/w 1-6  "))
								print("my batting run is  ",comp_batting_run)
								u += comp_batting_run
								if u > t:
									print("i won the game and my score is",u)
									sys.exit("the game is over")
								if bowling_run == comp_batting_run:
									if t < u:
										print("i won the game and my score is ",u)
										sys.exit("the game is over")
									if t > u:
										print("you won the game and my score is ",u)
										sys.exit("the game is over")									
						else:	
							pass
				if bat_bowl =="bowling":
					t = 0
					u = 0
					while True:
						bowling_run = int(input("enter your bowling run --->  "))
						comp_batting_run = (random.randint(1,6))
						print("my batting run is ---> ",comp_batting_run)
						t += comp_batting_run
						if comp_batting_run == bowling_run:
							print("i am out and my score is",t)
							print("now its your turn")
							while True:
								batting_run = int(input("enter your batting run ---> "))
								comp_bowling_run = (random.randint(1,6))
								print("my bowling run is ---> ",comp_bowling_run)
								u += batting_run
								if comp_bowling_run == batting_run:
									if t > u:
										print("i won the game and my score is",t)
										sys.exit("GAME OVER")
									if u > t:
										print("you won the game and your score is",u)
										sys.exit("GAME OVER")
								if u > t:
									print("you won the game and your score is",u)
									sys.exit("GAME OVER")
						else:
							continue
		if odd_even == "even":
			if addition_toss % 2 != 0:
				comp_choose = ["batting","bowling"]
				choice = comp_choose[randint(0,1)]
				print("i choose to",choice)
				if choice == "batting":
					t = 0
					u = 0
					while True:
						bowling_run = int(input("enter your bowling run --->  "))
						comp_batting_run = (random.randint(1,6))
						print("my batting run is ---> ",comp_batting_run)
						t += comp_batting_run
						if comp_batting_run == bowling_run:
							print("i am out and my score is",t)
							print("now its your turn")
							while True:
								batting_run = int(input("enter your batting run ---> "))
								comp_bowling_run = (random.randint(1,6))
								print("my bowling run is ---> ",comp_bowling_run)
								u += batting_run
								if comp_bowling_run == batting_run:
									if t > u:
										print("i won the game and my score is",t)
										sys.exit("GAME OVER")
									if u > t:
										print("you won the game and your score is",u)
										sys.exit("GAME OVER")
								if u > t:
									print("you won the game and your score is",u)
									sys.exit("GAME OVER")
						else:
							continue									
				if choice == "bowling":
					t = 0
					u = 0
					while True:
						batting_run =int(input("enter the batting run between 1-6  "))
						comp_run = (random.randint(1,6))
						print("my no.is ",comp_run)
						t += batting_run
						if batting_run == comp_run:
							print("you are out!!! and your score is",t)
							print("now its my turn")
							while True:
								comp_batting_run = int(random.randint(1,6))
								bowling_run = int(input("enter your bowling run b/w 1-6  "))
								print("my batting run is  ",comp_batting_run)
								u += comp_batting_run
								if u > t:
									print("i won the game and my score is",u)
									sys.exit("the game is over")
								if bowling_run == comp_batting_run:
									if t < u:
										print("i won the game and my score is ",u)
										sys.exit("the game is over")
									if t > u:
										print("you won the game and my score is ",u)
										sys.exit("the game is over")									
						else:	
							continue
		elif odd_even == "odd":
			if addition_toss % 2 == 0:
				comp_choose = ["batting","bowling"]
				choice = comp_choose[randint(0,1)]
				print("i choose to",choice)
				if choice == "batting":
					t = 0
					u = 0
					while True:
						bowling_run = int(input("enter your bowling run --->  "))
						comp_batting_run = (random.randint(1,6))
						print("my batting run is ---> ",comp_batting_run)
						t += comp_batting_run
						if comp_batting_run == bowling_run:
							print("i am out and my score is",t)
							print("now its your turn")
							while True:
								batting_run = int(input("enter your batting run ---> "))
								comp_bowling_run = (random.randint(1,6))
								print("my bowling run is ---> ",comp_bowling_run)
								u += batting_run
								if comp_bowling_run == batting_run:
									if t > u:
										print("i won the game and my score is",t)
										sys.exit("GAME OVER")
									if u > t:
										print("you won the game and your score is",u)
										sys.exit("GAME OVER")
								if u > t:
									print("you won the game and your score is",u)
									sys.exit("GAME OVER")
						else:
							continue									
				if choice == "bowling":
					t = 0
					u = 0
					while True:
						batting_run =int(input("enter the batting run between 1-6  "))
						comp_run = (random.randint(1,6))
						print("my no.is ",comp_run)
						t += batting_run
						if batting_run == comp_run:
							print("you are out!!! and your score is",t)
							print("now its my turn")
							while True:
								comp_batting_run = int(random.randint(1,6))
								bowling_run = int(input("enter your bowling run b/w 1-6  "))
								print("my batting run is  ",comp_batting_run)
								u += comp_batting_run
								if u > t:
									print("i won the game and my score is",u)
									sys.exit("the game is over")
								if bowling_run == comp_batting_run:
									if t < u:
										print("i won the game and my score is ",u)
										sys.exit("the game is over")
									if t > u:
										print("you won the game and my score is ",u)
										sys.exit("the game is over")									
						else:	
							continue											
	else:
		print("enter a number between 1 to 6")
		toss = int(input("enter a number for toss ---> "))