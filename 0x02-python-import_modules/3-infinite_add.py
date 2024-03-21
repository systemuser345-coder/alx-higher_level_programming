#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    add = 0
    arg_count = len(sys.argv)

    if arg_count <= 1:
        print("0")
    else:
        if arg_count >= 2:
            for i in range(1, arg_count):
                num = int(sys.argv[i])
                add += num
            print(add)
