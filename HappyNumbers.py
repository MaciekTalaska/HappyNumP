from __future__ import print_function
import sys

allhappy = list()
allsad = list()
happysad = dict()

slowhappysad = dict()
quickhappysad = dict()

def main(argv=None):
    if argv is None:
        argv = sys.argv
    if len(argv) < 3:
        print("range has not been specified. exiting...")
        sys.exit(-1)
    start = int(argv[1])
    stop = int(argv[2])
    if len(argv) > 3 and argv[3] == 's':
        for number in range(start, stop + 1):
            allnumbers = list()
            n = is_happy(number, allnumbers)
            slowhappysad[number] = n
            print("%s %s" % (number, n))
        print('all happy:')
        for i in slowhappysad.keys():
            if slowhappysad.get(i):
                print(str(i) +" ")
    if len(argv) > 3 and argv[3] == 'q':
        for number in range(start, stop + 1):
            allnumbers = list()
            n = is_happy_quick(number, allnumbers)
            quickhappysad[number] = n
            print("%s %s" % (number, n))
        print('all happy:')
        for number in quickhappysad.keys():
            if quickhappysad.get(number):
                print(str(number) + " ")
    if len(argv) > 3 and argv[3] == 'd':
        # pre-populate dictionary with empty items
        # does that make any sense at all?
        for number in range(start, stop + 1):
            happysad[number] = 0
        for number in range(start, stop + 1):
            allnumbers = list()
            n = is_happy_dict(number, allnumbers)
            print("%s %s" % (number, n))
        print('all happy:')
        for number in happysad.keys():
            if happysad[number] is True:
                print(str(number) + " ")


def is_happy(number, allnumbers):
    if number in allnumbers:
        allnumbers.append(number)
        return False
    allnumbers.append(number)
    if number == 1:
        return True
    if number == 0:
        return False
    characters = str(number)
    newnumber = 0
    for c in characters:
        partial = int(pow(int(c), 2))
        newnumber += partial
    return is_happy(newnumber, allnumbers)


def is_happy_dict(number, allnumbers):
    global happysad
    if number == 0:
        return False
    if number == 1:
        for i in allnumbers:
            happysad[i] = True
        happysad[number] = True
        return True
    if number in allnumbers:
        for i in allnumbers:
            happysad[i] = False
        happysad[number] = False
        return False
    value = happysad.get(number)
    allnumbers.append(number)
    if (value is not None) and (value != 0):
        for number in allnumbers:
            happysad[number] = value
        return happysad[number]
    characters = str(number)
    newnumber = 0
    for c in characters:
        partial = int(pow(int(c), 2))
        newnumber += partial
    return is_happy_dict(newnumber, allnumbers)


def is_happy_quick(number, allnumbers):
    global allsad
    global allhappy
    if number in allsad:
        populate_sad(allnumbers)
        return False
    if number in allnumbers:
        populate_sad(allnumbers)
        return False
    if number in allhappy:
        return True
    if number == 1:
        populate_happy(allnumbers)
        return True
    if number == 0:
        return False
    allnumbers.append(number)
    characters = str(number)
    newnumber = 0
    for c in characters:
        partial = int(pow(int(c), 2))
        newnumber += partial
    return is_happy_quick(newnumber, allnumbers)


def populate_sad(sequence):
    global allsad
    #allsad = list(set(allsad + sequence))
    #allsad.sort()
    populate(allsad, sequence)


def populate_happy(sequence):
    global allhappy
    #allhappy = list(set(allhappy+sequence))
    #allhappy.sort()
    populate(allhappy, sequence)


def populate(destination, source):
    for num in source:
        if num not in destination:
            destination.append(num)
    destination.sort()


def print_sequence(sequence):
    for i in range(len(sequence)):
        number = sequence[i]
        msg = ''
        if i < len(sequence) - 1:
            msg = str(number) + " -> "
        else:
            msg = str(number)
        print(msg, end='')
    print()

if __name__ == "__main__":
    main()
