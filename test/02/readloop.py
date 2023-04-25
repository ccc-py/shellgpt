import history

history.start()

while True:
    # 读取用户输入
    line = history.input(">>> ")
    line = line.strip()
    if line == "exit":
        break
    if line == "":
        continue

history.end()