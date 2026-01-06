from errors_handling.errorParse import ParseError


def check_keys(infos):
    keys = [
        "WIDTH",
        "HEIGHT",
        "ENTRY",
        "EXIT",
        "OUTPUT_FILE",
        "PERFECT"
        ]

    origin = []

    for value in infos.keys():
        origin.append(value)

    if set(origin) == set(keys):
        return True

    return False


def parse(filename):
    with open(filename, "r") as file:
        infos = {}
        size = ["WIDTH", "HEIGHT"]
        coord = ["ENTRY", "EXIT"]

        for ln in file:
            line = ln.strip()

            if not line or line.startswith("#"):
                continue

            try:
                line_result = line.split("=")

                if len(line_result) != 2:
                    raise ParseError("missing key or value")

                if line_result[1] == '':
                    raise ParseError("the key is empty")

                if line_result[0] in size:
                    try:
                        infos[line_result[0]] = int(line_result[1])
                    except ValueError:
                        print("Error: wrong key type")
                        return None

                elif line_result[0] in coord:
                    try:
                        coords = tuple(
                            int(v.strip()) for v in line_result[1].split(',')
                            )
                        if len(coords) != 2:
                            raise ParseError("value contains wrong number")
                        infos[line_result[0]] = coords
                    except ValueError:
                        print("Error: wrong value")
                        return None

                elif line_result[0] == "PERFECT":
                    if line_result[1] == "True":
                        infos[line_result[0]] = True
                    elif line_result[1] == "False":
                        infos[line_result[0]] = False
                    else:
                        raise ParseError("wrong key type")

                elif line_result[0] == "OUTPUT_FILE":
                    infos[line_result[0]] = line_result[1]
                else:
                    raise ParseError("wrong key")

            except ParseError as e:
                print(f"Error: {e}")
                return None

        check = check_keys(infos)
        if not check:
            print("Error: key miss")
            return None

        return infos
