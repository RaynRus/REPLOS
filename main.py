#added reminder in SummerSafe about you cant open 7 cases in SummerSafe, only sale.
#added command dir and dir instruct
#added two new cases
#added new game
import datetime
import sys
import time
import random
from random import randint
#from random import choice

# block = [
#     "q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "[", "]",
#     "a", "s", "d", "f", "g", "h", "j", "k", "l", ";", "'", "\n",
#     "z", "x", "c", "v", "b", "n", "m", ",", ".", "/",
#     "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
#     "*", "-", "=", '+', "|", "`",
#     "\t", " ", "shift", "windows", "alt", "esc", "backspace", "clrt"
# ]

# for key in block:
#     keyboard.block_key(key)

# while True:
#     pass
#     break

setupTime = randint(1, 2)


def runHelp(title):
    print(title)
    print('help')
    print('date')
    print('calc')
    print('game1')
    print('credits')
    print('settings')
    print('writer')
    print('osnews')
    print('osinfo')
    print('specific')
    print('game2')
    print('game3')
    print('dir')
    print('dirinstruct')
def runDate():
    print('| DATE |')
    current_date = datetime.datetime.today()
    print(current_date)
def runCalc():
    print('| CALCULATOR |')
    a = int(input('Input first number.\n'))
    b = int(input('Input second number.\n'))
    c = str(input('+, -, *, /\n'))

    if c == '+':
        print(f"Decied! {a + b}")
    elif c == '-':
        print(f"Decied! {a - b}")
    elif c == '*':
        print(f"Decied! {a * b}")
    elif c == '/':
        print(f"Decied! {a / b}")
def runGame1():
    print('| GAME 1 |')
    print('Hello! This is first game on ReplOs.')
    time.sleep(0.5)
    print('You need to think carefuly.')
    time.sleep(0.5)
    print('You wake up in the fast train. And the brakes failed! You can jump out, stay here, or start cry')
    time.sleep(0.5)
    quest = input('What will you do?').lower()
    if quest == 'jump out':
        print('You survide but you break your leg. The wictory!')
    elif quest == 'stay here':
        print('Because you were in the last carriage...')
        time.sleep(0.5)
        print('The train crashed into the wall,')
        time.sleep(0.5)
        print("And you didn't get a single scratch. A real victory!") 
    elif quest == 'start cry':
        print('You start cry but you were in the last crage. YOU SURVIVED!')
def runCredits():
    print('| CREDITS |')
    print('Developing by - aleksey5')
    print('Developing on - Replit')
def runSettings():
    print('| SETTINGS |')
    print("ReplOS")
    print(f'Owner {name}')
    print('Version: Beta')
def runWriter():
    print('| NOTEPAD |')
    while True:
        print('if you want to stop write stop')
        text = input()
        if text.lower() == 'stop':
            print('We stoping writerpad')
            time.sleep(0.3)
            break
def runOsNews():
    print('| NEWS |')
    print('24/02/24')
    print('ReplOs is Prototype') 
    print('26/03/24')
    print('ReplOs is beta')
    print('18/04/24')
    print('Fixing some bugs')
    print('23/06/24')
    print('Added game3: "CaseOpener" ')
    print('07/07/24')
    print('Fixing some bugs')
    print('Added new case to the game3: "Reploid" ')
    print('14/07/24')
    print('| To arms |')
    print('Added new skins to the case "Reploid" ')
    print('16/07/24')
    print('| Time to upgrade the bow |')
    print('Added new skins to Recoil collection')
    print('17/07/24')
    print('| The Summer |')
    print('Added new case to the game3: "SummerDrop" ')
    print('18/07/24')
    print('Fixed bug when case "SummmerDrop" is dont oppening')
    print('26/07/24')
    print('Aded new name to the game Case Openner: "RandomDrop" ')
    print('The code in the calculator function has been changed')
    print('27/07/24')
    print('Removed new name of Case Openner')
    print('02/08/24')
    print('| Lets end the holidays |')
    print('Added first safe to the case openner: "Safe" ')
    print('12/08/24')
    print('| New case |')
    print('Added new case: Breakout')
    print('27/08/24')
    print('| The LAUNCH! |')
    print('ReplOs is out of beta ')
    print('Added reminder in SummerSafe about you cant open 7 cases in SummerSafe, only sale.')
    print('Added command dir and dir instruct')
    print('Added two new cases to game3')
    print('Added new game')
def runOsInfo():
    print('|ReplOs(Replit Operating System)|')
    print('[ReplOS |v.1.0.0|Build by @aleksey5]')
    print('Beginig of developing is: 18/02/24')
def runSpecific():
    print('|SPECIFICATION|')
    print('RAM: 1GB')
    print('ROM: 200MB')
    print('CPU: Intel Xeon MP')
    print('GPU: GTX 250')
    print('Operating System: [ReplOS |v.1.0.0|Build by @aleksey5]')
def runGame2():
    print('| GAME 2|')
    print('This is second game on RelpOs')
    time.sleep(0.5)
    print('You need to think carefuly.')
    time.sleep(0.5)
    job = input('Your job?\n').lower()
    print(f'You are at a job interview to {job}.') 
    print('You were asked a question: Do you have any work experience?')
    call = input('You can say no, 5 years, or why do I need it?').lower()
    if call == 'no':
        print('Get out! A Real Loss.')
    if call == '5 years':
        print('We know you lying to us. Loss')
    if call == 'why do i need it':
        print('We agree with you, we will teach you everything! Victory!')
def runGame3():
    print('Hello this is case oppener')
    time.sleep(0.5)
    caseChoose = input(
        'Choose your case: Recoil, Reploid, Summer Drop, Summer Drop capsule, Breakout, Horizon, Hutsman\n'
    ).lower()
    if caseChoose == 'recoil':
        caseRecoil = [
                      'AUG | Storm: Uncommon',
                      'P90 | Storm: Uncommon',
                      'MP7 | Motherboard: Uncommon',
                      'UMP - 45 | Roadblock: Rare', 
                      'P90 | Vent Rush: Epic', 
                      'Revolver R8 | Crazy 8: Epic',
                      'AK - 47 | Leet Museo: Arcane',
                      'USP-S | Prinsteam: Arcane', 
                      'M9 BAYONET | Vanilla: Namlees',
                      'M9 BAYONET | Lore: Namlees',
                      'M9 BAYONET | Fade: Namlees',
                      'M9 BAYONET | Safari Mesh: Namlees'
                     ]
        caseRecoil_random = random.choice(caseRecoil)
        print(f'You win!: {caseRecoil_random}')
    elif caseChoose == 'reploid':
        caseReploid = [
                       'AK - 47 | African Grid: Uncommon', 
                       'AWP | The Viper: Epic', 
                       'Zeus | Olympus: Legendary',
                       'M4A1 - S | Hyper Beast: Arcane',
                       'AUG | Chameleon: Arcane',
                       'Driver Gloves | Black Tie: Namlees',
                       'Hand Wraps | CAUTION!: Namlees',
                       'Moto Gloves | Blood Pressure: Namlees',
                      ]
        caseReploid_random = random.choice(caseReploid)
        print(f'You win!: {caseReploid_random}')
    elif caseChoose == 'summer drop':
        caseSummerdrop = [
                          'Negev | Terrain: Uncommon',
                          'Desert Eagle | Night: Uncommon',
                          'USP - S | Forest Leaves: Uncommon',
                          'CZ75 - Auto | Distressed: Rare',
                          'P90 | Off World: Rare',
                          'P90 | Cocoa Rampage: Rare',
                          'P90 | Freight: Rare',
                          'AK - 47 | Cartel: Epic',
                          'AK - 47 | Ice Coaled: Epic',
                          'MP9 | Bulldozer: Epic',
                          'MAC - 10 | Graven: Epic',
                          'Gut knife | Lore: Namlees',
                          'Gut knife | Gamma Doppler: Namlees',
                          'Gut Knife | Vanilla: Namlees'
                         ]
        caseSummerdrop_random = random.choice(caseSummerdrop)
        print(f'You win!: {caseSummerdrop_random}')
    elif caseChoose == 'summer drop capsule':
        caseSDC = [
                   'Sticker | This Is Fine: Rare'
                   'Sticker | Chicken Lover: Rare'
                   'Sticker | Luck Skill: Rare'
                   'Sticker | Co Co Co: Rare'
                   'Sticker | Stan: Epic'
                   'Sticker | Joan: Epic'
                   'Sticker | Fire Serpent Surf K: Legendary'
                   'Sticker | Global Elite: Legendary'
                  ]
        caseSDC_random = random.choice(caseSDC)
        print(f'You win!: {caseSDC_random}')
    elif caseChoose == 'SummerSafe':
        caseSummerSafe = [
                          'Case | Operation Breakout Weapon Case: Rare',
                          'Case | Horizon Case: Rare',
                          'Case | Huntsman Weapon Case: Rare',
                          'Case | Chroma Case: Epic',
                          'Case | Chroma Case 2: Epic',
                          'Case | Croma Case 3: Epic',
                          'Case | Clutch: Legendary',
                          'Case | Kilowatt: Legendary',
                          'Collection | Cobblestone: Arcane',
                          'Collection | Dust 2(2021): Arcane'
                         ]
        caseSummerSafe_random = random.choice(caseSummerSafe)
        if caseSummerSafe_random == 'Case | Operation Breakout Weapon Case: Rare':
            print('You win!: Case | Operation Breakout Weapon Case: Rare')
        elif caseSummerSafe_random == 'Case | Horizon Case: Rare':
            print('You win!: Case | Operation Horizon Case: Rare')
        elif caseSummerSafe_random == 'Case | Huntsman Weapon Case: Rare':
            print('You win!: Case | Huntsman Weapon Case: Rare')
        else:
            print(f'You win!: {caseSummerSafe_random} (You cant open this case, only sale)')
    elif caseChoose == 'breakout':
        caseBreakout = [
                        'MP7 | Urban Hazard: Rare',
                        'Negev | Desert-Strike: Rare',
                        'UMP-45 | Labyrinth: Rare',
                        'P2000 | Ivory: Rare',
                        'SSG 08 | Abyss: Rare',
                        'CZ75-Auto | Tigris: Epic',
                        'PP-Bizon | Osiris: Epic',
                        'Nova | Koi: Epic',
                        'P250 | Supernova: Epic',
                        'Five-SeveN | Fowl Play: Legendary',
                        'Desert Eagle | Conspiracy: Legendary',
                        'Glock-18 | Water Elemental: Legendary',
                        'P90 | Asiimov: Arcane',
                        'M4A1-S | Cyrex: Arcane',
                        'Butterfly Knife | Fade: Namlees',
                        'Butterfly Knife | Vanilla: Namlees',
                        'Butterfly Knife | Slaughter: Namlees',
                        'Butterfly Knife | Safari Mesh: Namlees',
                       ]
        caseBreakout_random = random.choice(caseBreakout)
        print(f'You win!: {caseBreakout_random}')
    elif caseChoose == 'horizon':
        caseHorizon = [
                       'R8 Revolver | Survivalist: Rare',
                       'Dual Berettas | Shred: Rare',
                       'AUG | Amber Slipstream: Rare',
                       'MP9 | Capillary: Rare',
                       'Tec-9 | Snek-9: Rare',
                       'Glock-18 | Warhawk: Rare',
                       'P90 | Traction: Rare',
                       'G3SG1 | High Seas: Epic',
                       'MP7 | Powercore: Epic',
                       'CZ75-Auto | Eco: Epic',
                       'Nova | Toy Soldier: Epic',
                       'AWP | PAW: Epic',
                       'Sawed-Off | Devourer: Legendary',
                       'FAMAS | Eye of Athena: Legandary',
                       'M4A1-S | Nightmare: Legendary',
                       'Desert Eagle | Code Red: Arcane',
                       'AK-47 | Neon Rider: Arcane',
                       'Ursus Knife | Forest DDPAT: Namlees',
                       'Ursus Knife | Stained: Namlees',
                       'Ursus Knife | Urban Masked: Namlees',
                       'Ursus Knife | Night Stripe: Namlees',
                       'Ursus Knife | Blue Steel: Namlees',
                       'Ursus Knife | Boreal Forest: Namlees',
                       'Ursus Knife | Crimson Web: Namlees',
                       'Ursus Knife | Vanilla: Namlees',
                     ]
        caseHorizon_random = random.choice(caseHorizon)
        print(f'You win!: {caseHorizon_random}')
    elif caseChoose == 'hutsman':
        caseHutsman = [
                       'SSG 08 | Slashed: Rare',
                       'Galil AR | Kami: Rare',
                       'Tec-9 | Isaac: Rare ',
                       'CZ75-Auto | Twist: Rare',
                       'P2000 | Pulse: Rare',
                       'P90 | Module: Rare',
                       'AUG | Torque: Epic',
                       'PP-Bizon | Antique: Epic',
                       'XM1014 | Heaven Guard: Epic',
                       'MAC-10 | Tatter: Epic',
                       'SCAR-20 | Cyrex: Legendary',
                       'M4A1-S | Atomic Alloy: Legandary',
                       'USP-S | Caiman: Legendary',
                       'AK-47 | Vulcan: Arcane',
                       'M4A4 | Desert-Strike: Arcane',
                       'Huntsman Knife | Safari Mesh: Namlees',
                       'Huntsman Knife | Boreal Forest: Namlees',
                       'Huntsman Knife | Urban Masked: Namlees',
                       'Huntsman Knife | Forest DDPAT: Namlees',
                       'Huntsman Knife | Scorched: Namlees',
                       'Huntsman Knife | Scorched: Namlees',
                       'Huntsman Knife | Stained: Namlees',
                       'Huntsman Knife | Crimson Web: Namlees',
                       'Huntsman Knife | Vanilla: Namlees',
                       'Huntsman Knife | Blue Steel: Namlees',
                       'Huntsman Knife | Case Hardened: Namlees',
                       'Huntsman Knife | Slaughter: Namlees',
                       'Huntsman Knife | Fade: Namlees',
                      ]
        caseHutsman_random = random.choice(caseHutsman)
        print(f'You win!: {caseHutsman_random}')
    else:
        print('Unknow case: please, retry search.')
def runDir():
    print('| File Manager |')
    time.sleep(0.5)
    print('If you open file manager first time, please, read the instruction.')
    fManager_quest = input('C:/>')
    if fManager_quest == 'dir /a-r':
        print('The volume in device C does not have a label')
        time.sleep(0.5)
        print('Volume Serial Number: 1898-3600')
        time.sleep(0.8)
        print('27/08/24 00:00 <DIR> $Recycle.Bin')
        print('27/08/24 00:00     24autoexec.bat')
        print('27/08/24 00:00 <DIR> Boot')
        print('27/08/24 00:00 <DIR> Python')
        print('27/08/24 00:00 <DIR> Config.Msi')
        print('27/08/24 00:00    15Config.sys')
        print('27/08/24 00:00    15Config.datatime')
        print('27/08/24 00:00    15Config.time')
        print('27/08/24 00:00    15Config.random')
        print('27/08/24 00:00    15Config.keyboard')
        print('27/08/24 00:00 <DIR> help.exe')
        print('27/08/24 00:00 <DIR> datatime.exe')
        print('27/08/24 00:00 <DIR> calc.exe')
        print('27/08/24 00:00 <DIR> game1.exe')
        print('27/08/24 00:00 <DIR> datatime.exe')    
        print('27/08/24 00:00 <DIR> credits.exe')
        print('27/08/24 00:00 <DIR> datatime.exe')
        print('27/08/24 00:00 <DIR> settings.exe')
        print('27/08/24 00:00    15Config.settings')
        print('27/08/24 00:00 <DIR> writer.exe')
        print('27/08/24 00:00 <DIR> osnews.exe')
        print('27/08/24 00:00 <DIR> osinfo.exe')
        print('27/08/24 00:00 <DIR> specific.exe')
        print('27/08/24 00:00 <DIR> game2.exe')
        print('27/08/24 00:00 <DIR> game3.exe')
        print('27/08/24 00:00 <DIR> dir.exe')
        print('27/08/24 00:00 <DIR> dirinstruct.exe')
        print('27/08/24 00:00    15Config.dir')
def runDirinstruct():
    print('Welcome to File manager instruction')
    time.sleep(0.5)
    print('To view all computer files, write dir /a-r')
    print('Nice using ReplitOS')
def runGame4():
    print('| Game4 |')
    print('This is fourth game on the replos.')
    time.sleep(0.5)
    print('You need to think carefuly.')
    time.sleep(0.5)
    print('A cat came up to you your actions?(You can You can... Pet her, she got fleas, just leave.')
    quest = input('Your actions?\n').lower()
    if quest == 'pet her':
        print('You got a cold in the form of fleas. Real loss')
    elif quest == 'she got fleas':
        print('Since you realized that she had fleas, you left and didnt get sick. A real victory')
    elif quest == 'just leave':
        print('You just leave. Victory')

print(setupTime)
name = input("Hello! Whats your name?\n")
time.sleep(0.5)
print(f"{name} nice to meet you!")
time.sleep(0.5)
print(f"{name} now we will download important files in your computer(Please dont write anything).")
time.sleep(0.4)

toolbar_width = 40
sys.stdout.write("[%s]" % (" " * toolbar_width))
sys.stdout.flush()
sys.stdout.write("\b" * (toolbar_width + 1))
for _i in range(toolbar_width):
    time.sleep(1)
    sys.stdout.write("-")
    sys.stdout.flush()
sys.stdout.write("]\n")
print('WARNING: This new version of ReplOs because old version was blocked.')
time.sleep(0.5)
print('ReplOs[VERSION: 1.0]')
print(f"|Welcome [{name.capitalize()}!]|")
print('Input "help" to see list of all commands')

while True:
    command = input('C:/')
    if command == 'help':
        runHelp('|LIST OF COMMANDS|')
    elif command == 'date':
        runDate()
    elif command == 'calc':
        runCalc()
    elif command == 'game1':
        runGame1() 
    elif command == 'credits':
        runCredits()
    elif command == 'settings':
        runSettings()
    elif command == 'writer':
        runWriter()
    elif command == 'osnews':
        runOsNews()
    elif command == 'osinfo':
        runOsInfo()
    elif command == 'specific':
        runSpecific()
    elif command == 'game2':
        runGame2()
    elif command == 'game3':
        runGame3()
    elif command == 'dir':
        runDir()
    elif command == 'dirinstruct':
        runDirinstruct()
    else:
         print('Error 545454: Invalid command:/')
