from string import ascii_lowercase

def main():
    # Shift characters by 2 positions
    cipher = ('g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc '
              'dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr\'q ufw rfgq rcv'
              'r gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw'
              ' ml rfc spj.')
    url = 'map'
    translation = str.maketrans(ascii_lowercase, ascii_lowercase[2:] +
                                ascii_lowercase[:2])
    message = cipher.translate(translation)
    answer = url.translate(translation)
    print(message)
    print("Answer: " + answer)


if __name__ == '__main__':
    main()
