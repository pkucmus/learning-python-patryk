

def make_3sg_form(text):

    if text.endswith("y"):
        text = text[:-1]
        text = text + "ies"
        return text

    elif text.endswith(('o', 's', 'x','z')):
        text = text + "es"
        return text

    elif text.endswith(('ch', 'sh')):
        text = text + "es"
        return text

    else:
        text = text + "s"
        return text


print "fixes" == make_3sg_form("fix")
print "prints" == make_3sg_form("print")
print "flies" == make_3sg_form("fly")
print "wishes" == make_3sg_form("wish")
