while True:
    try:
        x = input()
        print(x)
    except EOFError:
        break