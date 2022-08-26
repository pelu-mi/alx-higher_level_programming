#!/usr/bin/python3
def main():
    pass


if __name__ == "__main__":
    # stuff only to run when not called via 'import' here
    import hidden_4

    for i in dir(hidden_4):
        if i.startswith("__"):
            continue
        print(i)
    main()
