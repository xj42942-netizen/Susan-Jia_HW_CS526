import os

def check_snowfall(filename):
    with open(filename, "r") as f:
        n = int(f.readline().strip())
        snow = list(map(int, f.readline().split()))
    total = sum(snow)
    for i in range(n - 2):
        if sum(snow[i:i+3]) > total / 2:
            return "YES"
    return "NO"

def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    results = []
    for i in range(1, 6):
        fname = f"snowfall_input{i}.txt"
        if os.path.exists(fname):
            ans = check_snowfall(fname)
            line = f"{fname} solution: {ans}"
            results.append(line)
            print(line)
    with open("answers_snowfall.txt", "w") as f:
        f.write("\n".join(results) + "\n")

if __name__ == "__main__":
    main()
