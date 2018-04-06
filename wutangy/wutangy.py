"""
wutangy.py
~~~~~~~~~

wutangy is a module that creates WuTang Clan inspired lorem ipsum text.

Enter the 36 Chambers of the Shaolin, WuTang Killah Bees on the swarm.
suuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu

RIP ODB.

:copyright: @ 2018
:author: elias julian marko garcia
:license: MIT, see LICENSE
:LYRICS: EXCLUSIVE INTELLECTUAL PROPERTY OF THE WUTANG CLAN. 
"""
import sys
from random import randint
from bars import (BRING_DA, SHAME_ON, CLAN_IN, SEVENTH_CHAMBER, CAN_IT_ALL,
                  DA_MYSTERY, AINT_NOTHING, CREAM, METHOD_MAN, PROTECT_YA,
                  TEARZ)

longAssList = (bringDa + shameOn + clanIn + seventhChamber + canItAll +
               daMystery + aintNuthing + cREAM + methodMan + protectYa + tearz)

first = filter(lambda x: x[0] == x[0].upper(), longAssList)

last = filter(lambda x: x[-1] == '?' or x[-1] == '!' or x[-1] == '.',
              longAssList)

rest = filter(
    lambda x: x[0] != x[0].upper() or x[-1] != '?' or x[-1] != '!' or x[-1] != '.',
    longAssList)


def sentence(size):
    print(first)


def wu(chambers=0):
    ipsum = []
    if not chambers:
        if (len(sys.argv) > 1):
            chambers = sys.argv[1]
        else:
            chambers = 5

    print('WUTANG COMING AT YOU IN DUE TIME')
