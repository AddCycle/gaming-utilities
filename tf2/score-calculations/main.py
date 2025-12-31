from collections import OrderedDict
# how much exp required for level up (per grade)

def get_key_at(dictionary: dict, i: int):
    cnt = 0
    for key in dictionary.keys():
        if cnt == i:
            return key
        cnt += 1

grades = OrderedDict({
    "civilian": 750,
    "freelance": 1250,
    "mercenary": 2000,
    "commando": 3000,
    "assassin": 4500,
    "elite": 7000
})

# just to know which tier you are based on your exp
tiers_max_exp = {
    1: 455500,
    2: 911000,
    3: 1366500,
    4: 1822000,
    5: 2277500,
    6: 2733000,
    7: 3188500,
    8: 3644000,
}

# { tier: { level: exp } }
lookup_table: dict[int, dict[int, int]] = {}

print("---- LEVELS ----")

previous_grade = next(iter(grades)) # first element
current_exp = 0

tiers = 8
for tier in range(1, tiers + 1):
    tier_lookup = {}
    current_level = 1

    # print()
    # print(f"---- TIER {tier} ----")
    # print()

    for grade in grades:
        xp_amount = grades.get(grade)

        # print()
        # print(f"---- {grade.capitalize()} {tier} ----")
        # print()

        for _ in range(25):
            tier_lookup[current_level] = current_exp
            # print(f"Level {current_level}: {current_exp} XP")

            current_level += 1
            if current_level <= 150:
                current_exp += xp_amount # type: ignore
    
    lookup_table[tier] = tier_lookup

user_exp = int(input("What is your current exp ?\n"))
user_kills = int(input("How many kills are you going to get ?\n"))

user_tier = 0
user_lvl = 0

for t, xp in tiers_max_exp.items():
    if xp < 0 or xp > 3644000:
        print("You are too far")
        exit()
    
    if xp < user_exp and t < 8:
        continue
    else:
        user_tier = t
        break

print(f"Your tier is {user_tier}")

for lookup_lvl, lookup_xp in lookup_table[user_tier].items():
    if user_exp < lookup_xp:
        continue
    else:
        user_lvl = lookup_lvl

user_grade = user_lvl // 25
print(f"Your are a : {get_key_at(grades, user_grade)}, lvl {user_lvl}")