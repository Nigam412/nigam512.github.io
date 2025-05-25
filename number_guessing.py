import random
secret_number=random.randint(1,10)
 
attempts=0
while attempts<5:
 number=int(input("Guess a number between 1 to 10\n"))
 
 attempts+=1
 if number==secret_number:
    print(f"🎉 Correct! You guessed it in {attempts} attempt(s).")
    break
else:
    print("❌ Wrong guess. Try again!")
    
    
