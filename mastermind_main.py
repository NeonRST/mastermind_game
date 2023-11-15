import master_class
run = True
playing = True
while run:
    print("Rules:")
    print("")
    row = int(input("how many rows would you like to play?: "))
    rn = int(input("how many numbers would you like to play?: "))
    dup = bool(input("would you like duplicates on or off? (True/False): "))
    ans = master_class.Mastermind(row, rn, dup)
    while playing:
        playing = master_class.Mastermind.playing(ans)
