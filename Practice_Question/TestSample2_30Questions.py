#8List
angle = -1
for i in range(1, -1):
    if 2 * 1 < 4:
        angle += 1
else:
    angle += 1
print(angle)

#9List
torque = 0
while torque != 0:
    torque //= 2
    print("*", end = "")
else:
    print("*")

#10List
others = 1
for i in range(2, 4):
    for j in range(-1, 2):
        if i == j:
            others += 1
        else:
            break
print(others)

#11List
power = 2
while power < 5:
    power += 1
    if power == 3:
        continue
    print("@", end = "")
else:
    print("@")

#15List
planeta = 1 + 2 * 3 // 4
if planeta < 0:
    print("#")
elif planeta > 2:
    print("##")
else:
    print("###")

#19List
answers = (False, True, True)
selection = answers[:]
points = 0
for answer in selection[1:]:
    if answer:
        points += 1
print(points)

#20List
train_speed = {"FlyingScotman": 201, "TGV": 320, "Shinkansen": 320}

for train in train_speed.items():
    print(train[0], end = "")

#21List
list_one = [1, 2]
list_two = list_one[:]
list_two.append(3)
print(list_one[-1]) + list_two[-1]

#23List
def process(data):
    data = 2
    return data

measurements = [0 for i in range(3)]
result = process(measurements)
print(result[-2])