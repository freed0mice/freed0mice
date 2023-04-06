import itertools


# 330
combinations = set(list(itertools.permutations("ВОДОПАД")))

print(combinations)
g = ["А", "О"]
res = 0
l = 0
for word in combinations:
    flag = True
    for i in range(0, len(word) - 1):
        if word[i] in g and word[i + 1] in g:
            flag = False
    if flag == True:
        res += 1
print(res)



# 328
s = list(itertools.product("СВЯТОЛА", repeat=7))
so = ["С", "В", "Т", "Л"]
gl = ["О", "Я", "А"]
res = 0
for elem in s:
    s = 0
    g = 0
    for letter in elem:
        if letter in so:
            s += 1
        else:
            g += 1
    if g > s:
        res += 1
print(res)
