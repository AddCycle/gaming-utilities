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
user_score = int(input("How many score are you going to get ?\n"))

bonus_exp = 0
if input("Will you finish the game ?\n") == "Yes":
    bonus_exp += 100
if input("Will you win ?\n") == "Yes":
    bonus_exp += 50
# points calculation must be in count TODO 6.5xp per point

user_tier = 0
user_lvl = 0

def get_tier_by(exp):
    for t, xp in tiers_max_exp.items():
        if xp < 0 or xp > 3644000:
            print("You are too far")
            exit()

        if xp < exp and t < 8:
            continue
        else:
            return t

user_tier = get_tier_by(user_exp)

print(f"Your tier is {user_tier}")

def get_lvl_by(p_tier, p_exp):
    lvl = -1
    for lookup_lvl, lookup_xp in lookup_table[p_tier].items():
        if lookup_xp <= p_exp:
            lvl = lookup_lvl
    return lvl

user_lvl = get_lvl_by(user_tier, user_exp)

user_grade = (user_lvl - 1) // 25

print(f"Your are a : {get_key_at(grades, user_grade)}, lvl {user_lvl}")

new_exp_amount = user_exp + user_score * 3 # 3 xp per score (avg)
new_tier = get_tier_by(new_exp_amount)
new_user_lvl = get_lvl_by(new_tier, new_exp_amount)
print(f"new exp amount {new_exp_amount}")
new_user_grade = (new_user_lvl - 1) // 25

print(f"Your will be a : {get_key_at(grades, new_user_grade)}, lvl {new_user_lvl}")