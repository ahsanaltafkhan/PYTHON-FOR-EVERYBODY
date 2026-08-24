"""\nWord Count\n\n"""\n\ntext = input("Enter a sentence: ").lower().split()
counts = {}
for word in text:
    counts[word] = counts.get(word, 0) + 1
print(counts)\n