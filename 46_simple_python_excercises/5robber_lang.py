CONSONNANT = (
    'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's',
    't', 'v', 'w', 'x', 'z'
)


def translate(text):
    output = ''
    for i in text:
        if i.lower() in CONSONNANT:
            output += '{0}o{0}'.format(i)
        else:
            output += i
    return output


print translate("This is fun")
print 'ToThohisos isos fofunon' == translate("This is fun")
