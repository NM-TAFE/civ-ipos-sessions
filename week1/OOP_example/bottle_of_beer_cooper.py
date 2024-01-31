def bottles_of_beer():
    bottles = 100
    while True:
        print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer")
        bottles -= 1
        
        if bottles == 0:
            break

bottles_of_beer()