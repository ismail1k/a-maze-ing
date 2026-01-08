def parse(filename):
    with open(filename, "r") as file:
        infos = {}
        digit = ["WIDTH", "HEIGHT"]
        coord = ["ENTRY", "EXIT"]

        for l in file:
            line = l.strip()

            if not line or line.startswith("#"):
                continue

            line_result = line.split("=")
            if len(line_result) != 2:
                print("Error")
                break

            if line_result[1] == '':
                print("error is empty")
                break

            if line_result[0] in digit:
                try:
                    infos[line_result[0]] = int(line_result[1])
                except ValueError:
                    print("Error: the info is wrong")
                    break
            elif line_result[0] in coord:
                try:
                    coords= tuple(int(v.strip()) for v in line_result[1].split(','))
                    infos[line_result[0]] = coords
                except ValueError:
                    print("Error: the info is wrong")
                    break
            elif line_result[0] == "PERFECT":
                if line_result[1] == "True":
                    infos[line_result[0]] = True
                else:
                    infos[line_result[0]] = False
            else:
                infos[line_result[0]] = line_result[1]
        return infos
        # for n, info in infos.items():
        #     print(f"key = {n} : value = {info}")
    
