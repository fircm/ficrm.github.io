from time import sleep


def ask():
    l = []
    i = input('请输入任意正整数：')
    l.append(int(i))
    if l[len(l) - 1] > 0:
        while True:
            if l[len(l) - 1] % 2 == 0:
                l.append(int(l[len(l) - 1] / 2))
                k = str(l[len(l) - 2]) + '÷2='
            else:
                l.append(int(l[len(l) - 1] * 3 + 1))
                k = str(l[len(l) - 2]) + '×3+1='
            print('当前结果：' + (25 - len(k)) * ' ' + k + '  ' + str(int(l[len(l) - 1])))
            sleep(0.05)
            if len(l) > 9:
                if l[-10:-1] == [4, 2, 1, 4, 2, 1, 4, 2, 1]:
                    print('程序结束-----------------------------------------')
                    return 0


while True:
    ask()
