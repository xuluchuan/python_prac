def file_ge(file):
    with open(file, encoding='utf-8') as f:
        for line in f:
            yield line.strip()


file_ge1 = file_ge('file')
for file_line in file_ge1:
    print("***" + file_line)
