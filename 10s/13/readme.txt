On this day, I spent an hour going through buggy code and fixing semantic and syntactic errors.  

An example of some of the bugs I was looking for:
```import random
comp_num = random.randint(1,100)
guess = input("Select a number between 1 and 100")
if guess = comp_num:
    print("You win!")
else:
    print("You lose!")
```
In this example, I found that the program needed to convert the guess into an integer in order to compare the guess to the computer number.  Additionally, we need to use '==' and not '=' when comparing.  So the corrected code should look liked:
```import random
comp_num = random.randint(1,100)
guess = int(input("Select a number between 1 and 100"))
if guess == comp_num:
    print("You win!")
else:
    print("You lose!")
```
