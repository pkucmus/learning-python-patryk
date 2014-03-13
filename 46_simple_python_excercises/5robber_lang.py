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
#consonant 'b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','z'
    # trans = ""
    # consonant = 'bcdfghjklmnpqrstvwxz'



    # for i in text.lower():
    #     if i in consonant:
    #         tr = "%so%s" % (i, i)
    #         trans = trans + tr

    #     else:
    #         trans = trans + i

    # return trans

print translate("This is fun")
print 'ToThohisos isos fofunon' == translate("This is fun")
