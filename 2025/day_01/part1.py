rots = open("./2025/input/day_1.txt").read()

rots = rots.strip().split("\n")

# print(" ".join(rots))

current = 50
zero_count = 0

for rot in rots:
    val = int(rot[1:])
    if rot.startswith("L"):
        current -= int(rot[1:])
    elif rot.startswith("R"):
        current += int(rot[1:])

    if current > 99 or current < 0: #* for instance: rotate to expected 14, if current = 314
        current = current % 100 #* basically remove the hundreds digit

        
    if current == 0:
        zero_count += 1

    print("dial is at:", current)

print("Final dial position:", current)
print("Zero count is      :", zero_count)