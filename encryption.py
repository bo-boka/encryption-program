def decode(x):
    word = ''
    index = 0
    numbs = "0123456789"
    while index < len(x):
        if x[index] in numbs:
            word += x[1 + index + int(x[index])]
        index += 1
    return word

#above is best version



def decode(x):
    """
        >>> decode("0h2abe1zy")
        'hey'
        >>> decode("2tkc0a4odkek1ee")
        'cake'
        >>> decode("3kdjb5dkgjeu2llt3dket")
        'butt'
        >>> decode("1df0u1rc0k")
        'fuck'
        >>> decode("6dkfkekt2kqe8dkwozcnws4iipvt2lkt0e4fjnns0t")
        'testtest'
    """
    newstring = ''
    xlist = []
    numlist = "0123456789"
    c = 0
    num = 0
    word = ''
    for char in x:
        if char in numlist:
            num += 1
    while c < num:
        if x[0] in numlist:
            xlist += [x[:2 + int(x[0])]]
            newstring = x[2 + int(x[0]):]
            x = newstring
            c += 1
    for element in xlist:
        word += element[int(element[0]) + 1]
    return word
                
if __name__ == '__main__':
    import doctest
    doctest.testmod()

print "pass"

