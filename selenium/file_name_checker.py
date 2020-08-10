import data

with open("selenium/fit_file.txt", "r") as file:
    for line in file:
        line = line.strip()
        uncorrected = 1
        for rename_pair in data.rename_pairs:
            if rename_pair in line:
                print(
                    line.replace(rename_pair, data.rename_pairs[rename_pair]) + " NEW"
                )
                uncorrected = 0

        if uncorrected:
            print(line)
