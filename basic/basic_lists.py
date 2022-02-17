fibonacci_list = [1, 2, 3, 5, 8, 13, 21]

for number in fibonacci_list:
    print(number, end=" ")

print()
user_name = "Vinicios"

for letter in user_name:
    print(f"{letter}:{ord(letter)}", end="|")
print()

months = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN",
          "JUL", "AGO", "SEP", "OCT", "NOV"]

months.append("DEC")

for month in months:
    print(f"{month}|{months.index(month) + 1}")

print()

months.reverse()
for month in months:
    print(f"{month}|{abs(months.index(month) - 12)}")
