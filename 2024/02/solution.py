def part_1():
    levels: list[list[int]] = []

    def check(l: list[int]) -> bool:
        for i in range(len(l) - 1):
            if not 1 <= l[i] - l[i + 1] <= 3:
                return False
        return True

    with open(file="input", mode="r", encoding="utf8") as h:
        while (l := [*map(int, h.readline().strip().split())]):
            levels.append(any([check(l), check(l[::-1])]))

    print(sum(levels))

def part_2():
    levels: list[list[int]] = []

    def check(l: list[int], skip: int = 0) -> bool:
        for i in range(len(l) - 1):
            if not 1 <= l[i] - l[i + 1] <= 3:
                return skip and any(check(l[j - 1:j] + l[j + 1:]) for j in (i, i + 1))
        return True

    with open(file="input", mode="r", encoding="utf8") as h:
        while (l := [*map(int, h.readline().strip().split())]):
            levels.append(check(l, 1) or check(l[::-1], 1))
    print(sum(levels))

part_1()
part_2()