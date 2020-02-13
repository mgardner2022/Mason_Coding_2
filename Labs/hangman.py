import random
hanging = ['''
 ________
 |      |
 |      |
        |
        |
        |
        |
 _______|
''',
'''
 ________
 |      |
 |      |
 O      |
        |
        |
        |
 _______|
''',
'''
 ________
 |      |
 |      |
 O      |
 |      |
        |
        |
 _______|
''',
'''
 ________
 |      |
 |      |
 O      |
 |\     |
        |
        |
 _______|
''',
'''
 ________
 |      |
 |      |
 O      |
/|\     |
        |
        |
 _______|
''',
'''
 ________
 |      |
 |      |
 O      |
/|\     |
  \     |
        |
 _______|
''',
'''
 ________
 |      |
 |      |
 O      |
/|\     |
/ \     |
        |
 _______|

''']


def split(word):
    return list(word)


words = ["breadstick", "meatloaf", "bananabread", "beans", "corn", "steak", "borscht"]
game_word = words[random.randrange(len(words))]
played_letters = []
game_letters = split(game_word)
level = 0
wins = 0

done = False
while not done:

    print(hanging[level])

    for letter in game_word:
        if letter in played_letters:
            print(letter, end=" ")
        else:
            print("__", end=" ")

    print("\nYou've tried: ", played_letters)
    guess = input("Pick a letter: ").lower()

    if guess in played_letters:
        print("You already guessed this.")
    elif len(guess) >= 2:
        print("One letter at a time")
    elif guess in game_letters:
        played_letters.append(guess)
        wins += game_word.count(guess.lower())
        print("You got it right!")
    else:
        played_letters.append(guess)
        level += 1
        print("Wrong.")

    if wins == len(game_word):
        print("You Win!")
        done = True

    if level == 6:
        print(hanging[6])
        print("You lose")
        done = True

