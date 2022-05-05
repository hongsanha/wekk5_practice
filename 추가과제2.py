sen=input("Enter a sentence: ")
sen=sen.lower()
vowels=0
vowels+=sen.count("a")
vowels+=sen.count("e")
vowels+=sen.count("i")
vowels+=sen.count("o")
vowels+=sen.count("u")
print(f"Your sentence contains {vowels} vowels.")