import os
def process_exclusions(exclusions_file, exclusions_wild_file):
    try:
        with open(exclusions_file, 'r') as infile, open(exclusions_wild_file, 'w') as outfile:
            for line in infile:
                stripped = line.strip()
                if stripped.startswith('||') and stripped.endswith('^'):
                    domain = stripped[2:-1]  # remove || and ^
                    if 1 <= domain.count('.') <= 2:
                        modified_line = line.replace('||', '||*.', 1)
                        outfile.write(modified_line)
        print(f"Processed file: {exclusions_wild_file}")
    except FileNotFoundError:
        print(f"Error: {exclusions_file} not found. Please ensure it exists.")
    except Exception as e:
        print(f"An error occurred: {e}")
process_exclusions('exclusions.txt', 'exclusions_wild.txt')
