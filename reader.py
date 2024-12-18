import ast

with open('harmeetsNumber.txt', 'r') as f:
    raw_data = f.read().strip()

raw_data = raw_data.replace('{', '[').replace('}', ']')

data_list = ast.literal_eval(raw_data)

result = {}

for name, value in data_list:
    if name not in result:
        result[name] = []
    result[name].append(value)

print(result)

for key, values in result.items():
    avg = sum(values) / len(values)
    print(f"{key} has an average score of {avg}")

