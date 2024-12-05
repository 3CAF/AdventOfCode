import re


def part_1():
    matrix: list[list[str]] = []
    matches: list[bool] = []

    test: str = ""
    text: list[str] = []
    line_length: int = 0
    strlen: int = 0
    max_column: int = 0
    search: str = "XMAS"
    

    with open(file="input", mode="r", encoding="utf8") as h:
        while (l := h.readline().strip()):
            test += l
            line_length = len(l)

    text = list(test)
            
    # find forward / backward column
    # fcm => find column match
    # lr = 0 normal(forward /backward)  1 = diag down right  -1 = diag down left
    # bw = 1 
    def fcm(text: list[str], srange: range, search: str, mtl: int, bw: int = 1, lr: int = 0):
        i: int = -1
        print("Search positions: ", range(srange.start, srange.stop * bw, ((srange.step + (1 * lr)) * bw)))
        for c in range(srange.start, srange.stop * bw, ((srange.step + (1 * lr)) * bw)):
            if c >= mtl or not c <= mtl or i >= len(search):
                return False
            if not text[c] == search[(i := i + 1)]:
                return False
            print(c, text[c])
            if text[c] == search[len(search) - 1]:
                return True
        return False if srange.start > srange.stop else True

    strlen = len(text)
    diag_right_max = len(search) * line_length
    max_column = line_length * len(search)
    print("Full length: ", strlen)

    [matches.append(True) for i in re.findall("(?=XMAS|SAMX)", test)]
    print(matches.count(True))
    
    # find column forward
    cnt = 0
    for i in re.finditer("X", test):
        cnt += 1
        i = i.start(0)
        if i != 19551:
            continue
        
        print(f"Found X [{cnt}] at: ", i)
        diagonal_length_right = line_length + 1
        # print(diag_right_max)
        diagonal_length_left = line_length - 1

        print("Is backward left diagonal: ", fcm(text, range(i, i+diag_right_max, line_length), search, strlen, -1, -1))
        matches.append(fcm(text, range(i, i+diag_right_max, line_length), search, strlen, -1, -1))
        print("Is backward right diagonal: ", fcm(text, range(i, i+diag_right_max, line_length), search, strlen, -1, 1))
        matches.append(fcm(text, range(i, i+diag_right_max, line_length), search, strlen, -1, 1))

        print("Is forward left diagonal: ", fcm(text, range(i, i+diag_right_max, line_length), search, strlen, 1, -1))
        matches.append(fcm(text, range(i, i+diag_right_max, line_length), search, strlen, 1, -1))
        print("Is forward right diagonal: ", fcm(text, range(i, i+diag_right_max, line_length), search, strlen, 1, 1))
        matches.append(fcm(text, range(i, i+diag_right_max, line_length), search, strlen, 1, 1))
        
        print("Is forward column match: ", fcm(text, range(i, max_column, line_length), search, strlen, 1, 0))
        matches.append(fcm(text, range(i, i+max_column, line_length), search, strlen, 1, 0))
        print("Is backward column match: ", fcm(text, range(i, max_column, line_length), search, strlen, -1, 0))
        matches.append(fcm(text, range(i, i+max_column, line_length), search, strlen, -1, 0))
        # break
    print("Matches", matches.count(True))
    # print(line_length)
    # print(text)



def part_2():
    pass

part_1()
part_2()