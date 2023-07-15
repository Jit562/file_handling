
# 1. Count the number of lines in the file.

with open('input.txt', 'r') as file:
    line_count = sum(1 for line in file)

print(f"Numbers in line in files:  {line_count}")  



# 2.	Count the number of words in the file.

with open('input.txt', 'r') as file:
    content = file.read()
    world_count = len(content.split())

print(f"Number of worlds in file:  {world_count}")    



# 3.	Count the number of occurrences of a specific word entered by the user.

with open('input.txt', 'r') as file:
    content = file.read()

user = input("Enter the word to search: ")
ocurrences = content.lower().count(user.lower())

print(f"Number of occurrences of '{user}': {ocurrences}")




# 4.	Create a new file named "output.txt" and write the contents of "input.txt" in reverse order.

input_file_path = 'input.txt'  
output_file_path = 'output.txt'

with open(input_file_path, 'r') as file:

    content = file.read()

reversed_content = content[::-1]


with open(output_file_path, 'w') as output_file:

    output_file.write(reversed_content)

print(f"Content of {input_file_path} written to {output_file_path} in reverse order.")   
