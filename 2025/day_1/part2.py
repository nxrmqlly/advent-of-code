# HEY YOU! YES YOU!
# I AM SORRY FOR BRUTEFORCE :(

rots = open("./day_1/input.txt").read()

rots = rots.strip().split("\n")

current = 50
zero_clicks = 0

for rot in rots:
    val = int(rot[1:])
    if rot.startswith("L"):
        for _ in range(0, val):
            current -= 1
            if current % 100 == 0:
                zero_clicks += 1

    elif rot.startswith("R"):
        for _ in range(0, val):
            current += 1
            if current % 100 == 0:
                zero_clicks += 1

    print("dial is at:", current)

print("Final dial position:", current)
# print("Zero count is      :", zero_count)
print("Zero clicks is     :", zero_clicks)
