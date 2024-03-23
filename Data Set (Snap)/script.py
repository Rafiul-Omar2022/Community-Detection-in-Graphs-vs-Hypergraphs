# code that write 1 in file

# amount = 16386
# with open("weights.txt", "w") as file:
#     file.write("1\n" * amount)


# extra tab cleaner and adding space between two strings
def clean_file(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    cleaned_lines = []
    for line in lines:
        # Replace tabs with spaces
        cleaned_line = line.replace('\t', ' ')

        # Include space between two strings
        cleaned_line = ' '.join(cleaned_line.split())

        cleaned_lines.append(cleaned_line)

    with open(output_file, 'w') as file:
        for line in cleaned_lines:
            file.write(line + '\n')


# Specify the input and output file paths
input_file = 'hyperedges.txt'
output_file = 'hyperedges.txt'

# Clean the file
clean_file(input_file, output_file)

print("Tabs replaced with spaces and extra spaces removed. Result saved to 'output.txt'")

