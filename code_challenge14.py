anime_list = []

while True:
    anime = input("Enter the title of an anime (Type 'exit' to finish) ---> ").lower()
    
    if anime == 'exit':
        print("You have exited the anime entry program....")
        print("Your Anime List Included:")
        break

    else:
        anime_list.append(anime)
        continue

for y in anime_list:
    print(f" - {y}")
    