#!/usr/bin/python3
def main():
    pass


if __name__ == "__main__":
    # stuff only to run when not called via 'import' here
    from sys import argv

    sum = 0
    if len(argv) == 1:
        print("0")
    else:
        for i in range(1, len(argv)):
            sum = sum + int(argv[i])
        print("{}".format(sum))
    main()
