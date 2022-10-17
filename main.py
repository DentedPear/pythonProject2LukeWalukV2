file1 = open("gradesv2.txt " , "r")

some_lines = file1.readlines()

for lines in some_lines:
        lines = lines.split(":")
        print(f"here is the {lines[2]}")