import sys


def dice(directory):
    sys.stdin = open(directory, "rt")
    n = int(input())
    prize = []
    for i in range(n):
        result = list(map(int, input().split()))
        if result[0]==result[1] & result[2]==result[1] & result[0]==result[2]:
            prize.append(10000 + result[0] * 1000)
        # how to remove redundancy...?
        elif result[0]==result[1] | result[2]==result[1] | result[0]==result[2]:
            if result[0]==result[1]:
                prize.append(1000 + result[0] * 100)
            elif result[2]==result[1]:
                prize.append(1000 + result[1] * 100)
            else:
                prize.append(1000 + result[2] * 100)
        else:
            prize.append(max(result) * 100)
    print(max(prize))

def main():
    source = "/Users/soo._.yonee/Desktop/Study/ESC/20SU_study/Python Algorithm_source code/섹션 2/9. 주사위 게임/in4.txt"
    dice(source)


if __name__ == "__main__":
    main()
