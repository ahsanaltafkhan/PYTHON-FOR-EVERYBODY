"""\nAverage Pattern\n\n"""\n\ntotal = 0
count = 0
while True:
    value = input("Enter a number (done to finish): ")
    if value.lower() == "done":
        break
    total += float(value)
    count += 1
print("Average:", total / count if count else 0)\n