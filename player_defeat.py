from player import *
import sys


def player_defeat():                                                                                                 
    print()
    print()
    print()                                                                                             
    print('   LOSE  U LO    U LOSE    LOSEY   LOSEY       YOU LO          YOU LO       OSEY      SEYOU LOSEY   ')
    print('  SEYO   OSEY   LOSEYOU   SEYOU   SEYOU         LOSEY         U LOSEYO    SEYOU LOSE  OU LOSEYOU L  ')
    print('    LO  YO    SEYO  LOSE  U L     U L           YOU         LOSE  U LO  YOU L  EYOU  LOSE    LOSE  ')
    print('     EY U L    OU     YOU   SE     OSE            L          EYO    SEY   LOSE         YOU          ')
    print('     U LOS     LOS     LOS  OU     YOU           SE         OU L    OU L  EYOU          LOSEY       ')
    print('      SEY     SEYO    SEYO  LO      LO           OU         LOSE    LOSE     OSEYO     SEYOU L      ')
    print('      OU       U L    OU    EYO    SEY           LOS         YOU    EYO       OU L     OU LOSE      ')
    print('      LOS      OSE    LOS   U L    OU           SEYO    SE    LO    U L        OSEY    LOS          ')
    print('      EYO      YOU   SEYO   OSEYOU LO            U L    OU   SEYO  LOSE  U LO  YOU     EYOU    EYO  ')
    print('     OU LO      LOSEYOU      OU LOSE            LOSEYOU LO    U LOSEYO   OSEYOU LOS   OU LOSE OU L  ')
    print('     LOSEY       YOU LO        SEYO            SEYOU LOSEY     SEYOU     YOU LOSEY    LOSEYOU LOSE  ')
    print()
    print()
    print('It seems you have been defeated. Quite a shame... whether through your own choices or the blade of some evil, it does not change the fact that you \nhave failed. The World of Men burns, and evils unspoken run rampant through the land, killing and terrorising everything. ')
    print("You  were a level " + str(player_stats["level"]), str(player_stats["class"]) + " named " + str(player_stats["name"]) + ".")
    print("You had " + ', '.join(player_inventory) + ".")
    print()
    input("Press ENTER to exit.")
    sys.exit()
    