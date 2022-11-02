rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random

weapon_list = [rock, paper, scissors]

p1weapon = weapon_list[random.randint(0,2)]
p2weapon = weapon_list[random.randint(0,2)]
print(f"Your Choice: {p1weapon}")
print(f"Computer Choice: {p2weapon}")

if p2weapon == p1weapon:
	print("Stalemate")
elif p1weapon == rock and p2weapon == scissors:
	print("You Win!")
elif p2weapon == rock and p1weapon == scissors:
	print("Computer Wins!")
elif p1weapon == scissors and p2weapon == paper:
	print("You Win!")
elif p2weapon == scissors and p1weapon == paper:
	print("Computer Wins!")
elif p1weapon == paper and p2weapon == rock:
	print("You Win!")
elif p2weapon == paper and p1weapon == rock:
	print("Computer  Wins!")

