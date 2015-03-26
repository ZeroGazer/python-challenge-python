from string import ascii_letters

def main():
    # Find rare characters
    message = open('2.txt', 'r').read()
    answer = [character for character in message if character in ascii_letters]
    print(''.join(answer))


if __name__ == '__main__':
    main()
