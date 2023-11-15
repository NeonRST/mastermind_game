import master_class
run = True
playing = True
while run:
    print("Rules:")
    print("A star 0 indicates that there is a number that is positioned correctly\n"
          "A letter X indicates that there is a number that is positioned incorrectly\n"
          "A _ indicates that there a number that is not present\n"
          "The game is played on until a player successfully solves the puzzle")
    print()
    row = int(input("how many positions would you like to play?: "))
    rn = int(input("how many numbers would you like to play?: "))
    dup = input("would you like duplicates on or off? (T/F): ")
    if dup == "T" or dup == "t":
        dup = True
    if dup == "F" or dup == "f":
        dup = False
    data = master_class.Mastermind(row, rn, dup)
    ans = master_class.Mastermind.menu(data)
    in_game = True
    while in_game:
        while playing:
            playing = master_class.Mastermind.playing(data)
        history = input("would you like to see your play history? (y/n): ")
        if history == "y" or history == "yes" or history == "Yes":
            for i in data.game_history:
                print(f"{i[0]} {i[1]}")


