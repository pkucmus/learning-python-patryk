
def beef_song():

    werses = [
        "{0} {bottle} of beer on the wall, {0} {bottle} of beer. \n",
        "Take one down, pass it around, {0} {bottle} of beer on the wall.\n"
    ]

    output = ''
    bottle = 'bottles'
    for ilosc in range(99, 0, -1):
        if ilosc == 1:
            bottle = "bottle"
            output += werses[0].format(ilosc, bottle=bottle)
            output += "no more beer on the wall!"
        else:
            output += werses[0].format(ilosc, bottle=bottle)
            output += werses[1].format(ilosc-1, bottle=bottle)

    return output

print beef_song()
