def log_save(log, time):
    print(time)
    with open("logs/log.txt ", "w") as file:
        for line in log:
            content = ""
            if not line:
                line = " [ Empty ] "
            if type(line) == str:
                if "*************" in line:
                    line += "\n\n"
            if (len(line) > 1 or type(line) == list) and type(line) != str:
                for item in line:
                    content += str(item) + ", "
                line = "\n"
            file.write(content + line)
        file.write("\n\n\nTime:\t\t" + f"{time:.8f}")
