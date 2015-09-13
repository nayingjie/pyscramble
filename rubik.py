import random, argparse
parser = argparse.ArgumentParser()
parser.add_argument("-c", "--cube",
                    dest="c",
                    type=str,
                    help="cube type",
                    metavar="CUBE",
                    required=False,
                    default="rubik"
                    )
parser.add_argument("-l", "--length",
                    dest="l",
                    type=int,
                    help="length of scramble",
                    metavar="LENGTH",
                    required=False,
                    default=25
                    )
parser.add_argument("-i", "--iterations",
                    dest="it",
                    type=int,
                    help="amount of scrambles",
                    metavar="AMOUNT",
                    required=False,
                    default=1
                    )
parser.add_argument("-n", "--notation",
                    dest="n",
                    type=str,
                    help="noatation (defaults to SiGN)",
                    metavar="NOTATION",
                    required=False,
                    default="SiGN"
                    )
isRubiksCube,isRubiksRevenge,isProfessorCube=False,False,False
a = parser.parse_args()
if a.c == "rubik":
    isRubiksCube = True
if a.c == "revenge":
    isRubiksRevenge = True
if a.c == "professor":
    isProfessorCube = True
#if a.c == "vcube6" or a.c == "6x6":
#    isVCubeSix = True
if a.n.lower() == "sign":
    useSiGN,useWCA = True,False
if a.n.lower() == "wca":
    useSiGN,useWCA = False,True
length = a.l
turnModifiers = ["", "\'", "2"]
alg = []
for i in xrange(a.it):
    del alg[:]
    if isRubiksCube: turns = ["R", "L", "U", "D", "F", "B"]
    if isRubiksRevenge and useSiGN or isProfessorCube and useSiGN: turns = ["R", "L", "U", "D", "F", "B", "2R", "2L", "2U", "2D", "2F", "2B", "r", "l", "u", "d", "f", "b"]
    if isRubiksRevenge and useWCA or isProfessorCube and useWCA:  turns = ["R", "L", "U", "D", "F", "B", "r", "l", "u", "d", "f", "b", "Rw", "Lw", "Uw", "Dw", "Fw", "Bw"]
    #if isVCubeSix and useSiGN:
    #        print "Oops - still waiting to get the SiGN notation for 6x6x6. Here's the WCA notation: http://www.randelshofer.ch/cubetwister/doc/notations/wca_6x6.html"
    #        print "Please run this program again with the argument for WCA (-n wca)."
    #        exit(1)
    #if isVCubeSix and useWCA: turns = ["R", "L", "U", "D", "F", "B", "r", "l", "u", "d", "f", "b", "Rw", "Lw", "Uw", "Dw", "Fw", "Bw", "3R", "3L", "3U", "3D", "3F", "3B"]
    for i in xrange(length):
        if alg == []:
            currentTurn = []
            currentTurn.append(random.choice(turns))
            currentTurn.append(random.choice(turnModifiers))
            alg.append("".join(currentTurn))
        else:
            lastTurn = alg[-1]
            cutUp = list(lastTurn)
            lTDirection = cutUp[0]
            currentTurn = []
            cTDirection = random.choice(turns)
            cTModifier = random.choice(turnModifiers)
            while cTDirection.upper() == lTDirection.upper():
                cTDirection = random.choice(turns)
            currentTurn.append(cTDirection)
            currentTurn.append(cTModifier)
            alg.append("".join(currentTurn))
    print " ".join(alg)
