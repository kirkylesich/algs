input_str = input()
cursor = 0
result = ""

for c in input_str:
    if c == '[':
        cursor = 0
    elif c == ']':
        cursor = len(result)
    else:
        result = result[:cursor] + c + result[cursor:]
        cursor += 1
print(result)