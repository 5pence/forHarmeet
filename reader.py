import ast

# open a file reader in reading mode
with open('harmeetsNumber.txt', 'r') as f:
    # remove spaces etc
    raw_data = f.read().strip()

# make raw_data like a 2d list
raw_data = raw_data.replace('{', '[').replace('}', ']')

# evaluate the string
data_list = ast.literal_eval(raw_data)

# create a empty dict
result = {}

# loop and add to dict
for name, value in data_list:
    if name not in result:
        result[name] = []
    result[name].append(value)

# now loop through and find average
# and print them for each item
for key, values in result.items():
    avg = sum(values) / len(values)
    print(f"{key} has an average score of {avg}")
