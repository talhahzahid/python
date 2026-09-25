tea_varieties = ["Black", "Green", "Oolong", "White"]

# print(tea_varieties[-1])
# print(tea_varieties[1])
# print(tea_varieties[1:3])
# tea_varieties[3] = 'Herbal'
# print(tea_varieties)
tea_varieties[1:2] = ["Lemon"]
# print(tea_varieties)
tea_varieties[1:3] = ["green", "herbal"]
# print(tea_varieties)
# print(tea_varieties[1:1])  # return empty array
tea_varieties[1:1] = ["test", "test", "test"]
# print(tea_varieties)
tea_varieties[1:4] = []
print(tea_varieties)
# for tea in tea_varieties:
#     print(tea)
# for tea in tea_varieties:
#     print(tea , end="-")
if "Oolong" in tea_varieties:
    print("I have Oolong tea")

tea_varieties.append("Oolong")  # add value on last
if "Oolong" in tea_varieties:
    print("I have Oolong tea")


tea_varieties.pop()  # remove last element from list
print(tea_varieties)
tea_varieties.remove("green")  # remove exact element which you want
print(tea_varieties)
tea_varieties.insert(1, "green")
print(tea_varieties)
