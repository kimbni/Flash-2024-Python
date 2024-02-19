import random

print("I am think of a number from 1-100.")
num = random.randint(1, 100)
count = 0
guess = 0

while guess != num:
  guess = int(input("\nGuess a number: "))
  count += 1
  if guess > num:
    print("Too high. Try again.")
  elif guess < num:
    print("Too low. Try again.")
  else:
    break
print(f"You got it! It took you {count} tries.")
