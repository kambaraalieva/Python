table = []
for i in range(1, 11):
    row = ""
    for j in range(1, 11):
        row += f"{i*j:4}"
    table.append(row)

for r in table:
    print(r)
