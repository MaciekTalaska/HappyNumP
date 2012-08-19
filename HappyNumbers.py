from __future__ import print_function
import math
import sys
import getopt

allhappy = list()
allsad = list()

def main(argv=None):
    if argv is None:
	argv = sys.argv
    if len(argv) < 3:
	print("range has been specified. exiting...")
	sys.exit(-1)
    start = int(argv[1])
    stop = int(argv[2])
    if len(argv) > 3 and argv[3] == 's':
        for number in range(start, stop+1):
	    allnumbers = list()
	    n = is_happy(number, allnumbers)
	    print( "%s %s" % (number, n))
    else:
        for number in range(start, stop+1):
	    allnumbers = list()
	    n = is_happy_quick(number, allnumbers)
	    print("%s %s" % (number, n))

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

def is_happy_quick( number, allnumbers):
    global allsad
    global allhappy
    if number in allsad:
	populate_sad(allnumbers)
	return False
    if number in allnumbers:
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
	partial = int(pow(int(c),2))
	newnumber += partial
    return is_happy_quick(newnumber, allnumbers)

def populate_sad( sequence ):
    global allsad
    populate(allsad, sequence)
    
def populate_happy( sequence):
    global allsad
    populate(allhappy, sequence)
    
def populate( destination, source):
    for num in source:
	if num not in destination:
	    destination.append(num)
    destination.sort()
    

def print_sequence( sequence ):
    for i in range(len(sequence)):
	number = sequence[i]
	msg = ''
	if i < len(sequence)-1:
	    msg = str(number) + " -> "
	else:
	    msg = str(number)
	print( msg, end='' )
    print()

if __name__ == "__main__":
    main()
