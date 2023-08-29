input_file_path = "data\eng-urdu.txt"
output_file_path = "data\processed\processed_eng-urdu.txt"

with open(input_file_path, "r", encoding="utf-8") as input_file, \
     open(output_file_path, "w", encoding="utf-8") as output_file:
    for line in input_file:
        parts = line.strip().split("\t")
        if len(parts) >= 2:
            text = "\t".join(parts[:2])  # Join the first two parts with a tab separator
            output_file.write(text + "\n")