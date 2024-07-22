num_bottles = 99

while num_bottles > 0:
    if num_bottles == 1:
        print(f"{num_bottles} bottle of beer on the wall, {num_bottles} bottle of beer.")
        print("Take one down and pass it around, no more bottles of beer on the wall.")
    else:
        print(f"{num_bottles} bottles of beer on the wall, {num_bottles} bottles of beer.")
        print(f"Take one down and pass it around, {num_bottles - 1} bottles of beer on the wall.")

    print()
    num_bottles -= 1

print("No more bottles of beer on the wall, no more bottles of beer.")
print("Go to the store and buy some more, 99 bottles of beer on the wall.")
