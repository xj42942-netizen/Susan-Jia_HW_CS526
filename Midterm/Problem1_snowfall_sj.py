import os

def check_snowfall(filename):
    with open(filename, "r") as f:
        n = int(f.readline().strip())
        cumulative = list(map(int, f.readline().split()))
    
    total = cumulative[-1]
    
    for i in range(n - 2):
        start = cumulative[i-1] if i > 0 else 0
        window = cumulative[i+2] - start
        
        if window > total / 2:
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
        f.write("\n".join(results))

if __name__ == "__main__":
    main()
