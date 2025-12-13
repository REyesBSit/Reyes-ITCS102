print("Welcome to the Manga Reader Recommender!")
print("Answer a few question to find your next read")
genre = input ("What Genre do you prefer? (action, romance, horror): ")

if genre == 'action':
    genre_duration = input ("How long should the manga be? (short, medium, long): ")

    if genre_duration == 'short':
        genre_decade = input ("Which Decade? (2000's or 2010's): ")

        if genre_decade == '2000':
            print("The system recommends 'action_short_2000' based from your preference, Happy Reading!!!")
        elif genre_decade == '2010':
            print("The system recommends 'action_short_2010' based from your preference, Happy Reading!!!")
        else:
            print("Decade Selected is not available at the moment, Please Try Again!!!")
    
    elif genre_duration == 'medium':
        genre_decade = input ("Which Decade? (2000's or 2010's): ")

        if genre_decade == '2000':
            print("The system recommends 'action_medium_2000' based from your preference, Happy Reading!!!")
        elif genre_decade == '2010':
            print("The system recommends 'action_medium_2010' based from your preference, Happy Reading!!!")
        else:
            print("Decade Selected is not available at the moment, Please Try Again!!!")
    
    elif genre_duration == 'long':
        genre_decade = input ("Which Decade? (2000's or 2010's): ")

        if genre_decade == '2000':
            print("The system recommends 'action_long_2000' based from your preference, Happy Reading!!!")
        elif genre_decade == '2010':
            print("The system recommends 'action_long_2010' based from your preference, Happy Reading!!!")
        else:
            print("Decade Selected is not available at the moment, Please Try Again!!!")
    
    else:
        print("Invalid Output, Please Try Again Later!!!")

elif genre == 'romance':
    genre_duration = input ("How long should the manga be? (short, medium, long): ")

    if genre_duration == 'short':
        genre_decade = input ("Which Decade? (2000's or 2010's): ")

        if genre_decade == '2000':
            print("The system recommends 'romance_short_2000' based from your preference, Happy Reading!!!")
        elif genre_decade == '2010':
            print("The system recommends 'romance_short_2010' based from your preference, Happy Reading!!!")
        else:
            print("Decade Selected is not available at the moment, Please Try Again!!!")
    
    elif genre_duration == 'medium':
        genre_decade = input ("Which Decade? (2000's or 2010's): ")

        if genre_decade == '2000':
            print("The system recommends 'romance_medium_2000' based from your preference, Happy Reading!!!")
        elif genre_decade == '2010':
            print("The system recommends 'romance_medium_2010' based from your preference, Happy Reading!!!")
        else:
            print("Decade Selected is not available at the moment, Please Try Again!!!")
    
    elif genre_duration == 'long':
        genre_decade = input ("Which Decade? (2000's or 2010's): ")

        if genre_decade == '2000':
            print("The system recommends 'romance_long_2000' based from your preference, Happy Reading!!!")
        elif genre_decade == '2010':
            print("The system recommends 'romance_long_2010' based from your preference, Happy Reading!!!")
        else:
            print("Decade Selected is not available at the moment, Please Try Again!!!")

    else:
        print("Invalid Output, Please Try Again Later!!!")

elif genre == 'horror':
    genre_duration = input ("How long should the manga be? (short, medium, long): ")

    if genre_duration == 'short':
        genre_decade = input ("Which Decade? (2000's or 2010's): ")

        if genre_decade == '2000':
            print("The system recommends 'horror_short_2000' based from your preference, Happy Reading!!!")
        elif genre_decade == '2010':
            print("The system recommends 'horror_short_2010' based from your preference, Happy Reading!!!")
        else:
            print("Decade Selected is not available at the moment, Please Try Again!!!")

    elif genre_duration == 'medium':
        genre_decade = input ("Which Decade? (2000's or 2010's): ")

        if genre_decade == '2000':
            print("The system recommends 'horror_medium_2000' based from your preference, Happy Reading!!!")
        elif genre_decade == '2010':
            print("The system recommends 'horror_medium_2010' based from your preference, Happy Reading!!!")
        else:
            print("Decade Selected is not available at the moment, Please Try Again!!!")

    elif genre_duration == 'long':
        genre_decade = input ("Which Decade? (2000's or 2010's): ")

        if genre_decade == '2000':
            print("The system recommends 'horror_long_2000' based from your preference, Happy Reading!!!")
        elif genre_decade == '2010':
            print("The system recommends 'horror_long_2010' based from your preference, Happy Reading!!!")
        else:
            print("Decade Selected is not available at the moment, Please Try Again!!!")
    
    else:
        print("Invalid Output, Please Try Again Later!!!")

else:
    print("Genre Selected Not Available, Try Again Later!!!")
