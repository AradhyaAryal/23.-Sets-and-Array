snack_box_A = {"chips", "cookies", "apple"}
snack_box_B = {"apple", "banana", "chips"}

snack_box_A.add("granola")
snack_box_B.add("pretzels")

shared = snack_box_A.intersection(snack_box_B)
print(shared)

counts = [5, 3, 8, 5]
counts.append(7)
counts.append(5)

print(counts.count(5))
counts.reverse()
print(counts)
