while True:
    try: 
        new_word = input("Please type an integer: ")
        print(int(new_word))
        break
    except ValueError:
        print("Please try again!")