import re 

def part_1():
    lines: list[str] = []
    
    with open(file="input", mode="r", encoding="utf8") as h:
        while (l := h.readline().strip()): lines.append(
            sum([st[0] * st[1] for s in re.findall("(?<=mul\()\d{1,3},\d{1,3}(?=\))", l) if (st:=[*map(int, s.split(","))])])
        )

    print(sum(lines))

def part_2():
    line = ""
    enabled: bool = True

    with open(file="input", mode="r", encoding="utf8") as h:
        while (l := h.readline().strip()): line += l

    print(sum(
        (s := [*map(int, re.findall(r"\d{1,3},\d{1,3}", instr)[0].split(","))])[0] * s[1]
        for instr in re.findall("do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\)", line)
        if (enabled := (
            False if instr.upper() == "DON'T()" else
            True if instr.upper() == "DO()" else enabled
        )) and re.search(r"\d{1,3},\d{1,3}", instr)
    ))

part_1()
part_2()