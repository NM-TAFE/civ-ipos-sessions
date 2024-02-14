def bottles_of_beer():
    bottles = 100
    while True:
        if bottles > 1:
            print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer")
            bottles -= 1
        
        elif bottles == 1:
            print(f"{bottles} bottle of beer on the wall, {bottles} bottle of beer")
            bottles -= 1

        if bottles == 0:
            print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer")
            break

bottles_of_beer()
