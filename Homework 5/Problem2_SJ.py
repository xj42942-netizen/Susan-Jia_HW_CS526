def count_vowel_combinations(morse_sequence):
    morse_sequence = morse_sequence.strip()
    
    if not morse_sequence:
        return 0
    
    vowel_codes = ['.-', '.', '..', '---', '..-']
    
    n = len(morse_sequence)
    dp = [0] * (n + 1)
    dp[0] = 1
    
    for i in range(1, n + 1):
        for code in vowel_codes:
            code_len = len(code)
            if i >= code_len:
                if morse_sequence[i - code_len:i] == code:
                    dp[i] += dp[i - code_len]
    
    return dp[n]


def read_morse_from_file(filename):
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
            if len(lines) >= 2:
                morse = lines[1].strip()
                return morse
            else:
                print(f"Error: File {filename} has incorrect format")
                return None
    except FileNotFoundError:
        print(f"Error: File {filename} not found")
        return None


def main():
    test_files = ['vowel_input1.txt', 'vowel_input2.txt', 
                  'vowel_input3.txt', 'vowel_input4.txt']
    
    for filename in test_files:
        morse_sequence = read_morse_from_file(filename)
        
        if morse_sequence is not None:
            result = count_vowel_combinations(morse_sequence)
            print(f"File Input: {filename}")
            print(f"The Number of Vowel combinations is: {result}")
        else:
            print(f"File Input: {filename}")
            print("Could not read file")


if __name__ == "__main__":
    main()
