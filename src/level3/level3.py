from re import findall

def main():
    # Find a small letter surrounded by 3 capital characters on each sides
    message = open('3.txt', 'r').read()
    pattern = '[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]'
    answer = findall(pattern, message)
    print(answer)


if __name__ == '__main__':
    main()
