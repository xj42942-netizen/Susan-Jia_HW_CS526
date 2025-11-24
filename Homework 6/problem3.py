import os

def clean_lines(lines):
    cleaned = []
    for line in lines:
        line = line.strip().replace("\ufeff", "")
        if line:
            cleaned.append(line)
    return cleaned

def load_preferences(filename):
    with open(filename, "r", encoding="utf-8") as f:
        raw = clean_lines(f.readlines())

    n = int(raw[0])
    men_raw = raw[1 : 1 + n]
    women_raw = raw[1 + n : 1 + 2*n]

    man_names = [line.split()[0] for line in men_raw]
    woman_names = [line.split()[0] for line in women_raw]

    man_to_id = {name: str(i+1) for i, name in enumerate(man_names)}
    woman_to_id = {name: str(i+1) for i, name in enumerate(woman_names)}

    men_prefs = {}
    women_prefs = {}

    for line in men_raw:
        parts = line.split()
        man = man_to_id[parts[0]]
        men_prefs[man] = [woman_to_id[w] for w in parts[1:]]

    for line in women_raw:
        parts = line.split()
        woman = woman_to_id[parts[0]]
        women_prefs[woman] = [man_to_id[m] for m in parts[1:]]

    return men_prefs, women_prefs, n, man_names, woman_names

def gale_shapley(men_prefs, women_prefs, n):
    women_rank = {
        w: {man: rank for rank, man in enumerate(pref)}
        for w, pref in women_prefs.items()
    }

    free_men = list(men_prefs.keys())
    next_proposal = {m: 0 for m in men_prefs}
    engagements = {}

    while free_men:
        m = free_men.pop(0)
        w = men_prefs[m][next_proposal[m]]
        next_proposal[m] += 1

        if w not in engagements:
            engagements[w] = m
        else:
            current = engagements[w]
            if women_rank[w][m] < women_rank[w][current]:
                engagements[w] = m
                free_men.append(current)
            else:
                free_men.append(m)

    return engagements

def restore_output(engagements, man_names, woman_names):
    man_map = {str(i+1): man_names[i] for i in range(len(man_names))}
    woman_map = {str(i+1): woman_names[i] for i in range(len(woman_names))}

    result = []
    for w in sorted(engagements, key=lambda x: int(x)):
        m = engagements[w]
        result.append(f"{man_map[m]} {woman_map[w]}")
    return result

def main():

    print("You will enter 3 input filenames.\n")

    for step in range(1, 4):
        filename = input(f"Enter input filename #{step}: ").strip()

        if not os.path.exists(filename):
            print(f"Error: {filename} not found.\n")
            continue

        print("\n====================================")
        print(f"Processing: {filename}")

        men_prefs, women_prefs, n, man_names, woman_names = load_preferences(filename)
        engagements = gale_shapley(men_prefs, women_prefs, n)
        result = restore_output(engagements, man_names, woman_names)

        print("\nStable Matching:")
        for line in result:
            print(line)


if __name__ == "__main__":
    main()
