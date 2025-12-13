music = True

while music == True:
    play = input("Would you like to play/continue your favorite song? ---> ").lower()

    if play == 'yes':
        print("Your Song Plays Successfully")
        continue

    else:
        print("Music Player Shutting Down...")
        break