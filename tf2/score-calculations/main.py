# how much exp required for level up (per grade)
grades = {
    "civilian": 750,
    "freelance": 1250,
    "mercenary": 2000,
    "commando": 3000,
    "assassin": 4500,
    "elite": 7000
}

print("---- LEVELS ----")

previous_grade = next(iter(grades)) # first element
current_exp = 0

tiers = 8
for tier in range(1, tiers + 1):
    current_level = 1

    print()
    print(f"---- TIER {tier} ----")
    print()

    for grade in grades:
        xp_amount = grades.get(grade)

        print()
        print(f"---- {grade.capitalize()} ----")
        print()

        for _ in range(25):
            print(f"Level {current_level}: {current_exp} XP")
            current_exp += xp_amount # type: ignore

            current_level += 1

            if current_level > 150:
                current_exp -= xp_amount # type: ignore