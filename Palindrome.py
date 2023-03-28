with open('words_in_english_dictionary.txt') as text:
    for line in text:
        line = line.strip()
        line2 = line[::-1]
        if line == line2:
            print(line)
            print ('Palindrome!')