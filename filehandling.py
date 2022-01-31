filepath1 = ""
filepath2 = ""
with open(filepath1,'r') as f1:
    for line in f1:
        with open(filepath2,'w') as f2:
            f2.write(line)
            fun = f2.seek(20)
        f2.close()
    f1.close()