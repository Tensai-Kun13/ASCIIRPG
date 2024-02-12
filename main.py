import os, random

run = True
menu = True
play = False
rules = False
key = False
fight = False
standing = True

HP = 50
HPMAX = HP
ATK = 3
pot = 1
elix = 0
gold = 0
x = 0
y = 0

       #   x = 0       x = 1       x = 2      x = 3      x = 4       x = 5       x = 6
map = [["plains",   "plains",   "plains",  "plains",  "forest", "mountain",     "cave"],  # y = 0
       ["forest",   "forest",   "forest",  "forest",  "forest",    "hills", "mountain"],  # y = 1
       ["forest",   "fields",   "bridge",  "plains",   "hills",   "forest",    "hills"],  # y = 2
       ["plains",     "shop",     "town",   "major",  "plains",    "hills", "mountain"],  # y = 3
       ["plains",   "fields",   "fields",  "plains",   "hills", "mountain", "mountain"]]  # y = 4

y_len = len(map) - 1
x_len = len(map[0]) - 1

biom = {
    "plains": {
        "t": "PLAINS",
        "e": True},
    "forest": {
        "t": "WOODS",
        "e": True},
    "fields": {
        "t": "FIELDS",
        "e": False},
    "bridge": {
        "t": "BRIDGE",
        "e": True},
    "town": {
        "t": "TOWN CENTRE",
        "e": False},
    "shop": {
        "t": "SHOP",
        "e": False},
    "major": {
        "t": "MAJOR",
        "e": False},
    "cave": {
        "t": "CAVE",
        "e": False},
    "mountain": {
        "t": "MOUNTAIN",
        "e": True},
    "hills": {
        "t": "HILLS",
        "e": True}
}

e_list = ["Goblin", "Orc", "Slime"]

mobs = {
    "Goblin": {
        "hp": 15,
        "at": 3,
        "go": 8
    },
    "Orc": {
        "hp": 35,
        "at": 5,
        "go": 18
    },
    "Slime": {
        "hp": 30,
        "at": 2,
        "go": 12
    },
    "Dragon": {
        "hp": 100,
        "at": 8,
        "go": 100
    }
}

current_tile = map[y][x]
print(current_tile)
name_of_tile = biom[current_tile]["t"]
print(name_of_tile)
enemy_tile = biom[current_tile]["e"]
print(enemy_tile)


def clear():
    os.system("cls")


def draw():
    print("xX--------------------------Xx")


def save():
    stat_list = [
        name,
        str(HP),
        str(ATK),
        str(pot),
        str(elix),
        str(gold),
        str(x),
        str(y),
        str(key)
    ]

    f = open("load.txt", "w")

    for item in stat_list:
        f.write(item + "\n")
    f.close()


def heal(amount):
    global HP
    if HP + amount < HPMAX:
        HP += amount
    else:
        HP = HPMAX
    print(f"{name}'s HP refilled to {HP}!")


def battle():
    global fight, play, run, HP, pot, elix, gold

    enemy = random.choice(e_list)
    hp = mobs[enemy]["hp"]
    hpmax = hp
    atk = mobs[enemy]["at"]
    g = mobs[enemy]["go"]

    while fight:
        clear()
        draw()
        print(f"Defeat the {enemy}!")
        draw()
        print(f"{enemy}'s HP: {hp}/{hpmax}")
        print(f"{name}'s HP: {HP}/{HPMAX}")
        print(f"POTIONS: {pot}")
        print(f"ELIXER: {elix}")
        draw()
        print("1 - ATTACK")
        if pot > 0:
            print("2 - USE POTION (30HP")
        if elix > 0:
            print("3 - USE ELIXER (50HP")
        draw()

        choice = input("# ")

        if choice == 1:
            hp -= ATK
            print(f"{name} dealt {ATK} damage to the {enemy}.")
            if hp > 0:
                HP -= atk
                print(f"{enemy} dealt {atk} damage to the {name}.")
            input("> ")

        elif choice == 2:
            if pot > 0:
                pot -= 1
                heal(30)
                HP -= atk
                print(f"{enemy} dealt {atk} damage to the {name}.")
            else:
                print("No potions!")
            input("> ")

        elif choice == 3:
            pass

        if HP <= 0:
            print (f"{enemy} defeated {name}...")
            draw()
            fight = False
            play = False
            run = False
            print("GAME OVER")
            input("> ")

        if hp <= 0:
            print(f"{name} defeated the {enemy}")
            draw()
            fight = False
            gold += g
            print(f"You've found {g} gold!")
            if random.randint(0, 100) < 30:
                pot += 1
                print("You've found a potion!")
            input("> ")
            clear()


while run:
    while menu:
        clear()
        draw()
        print("1, NEW GAME")
        print("2, LOAD GAME")
        print("3, RULES")
        print("4, QUIT GAME")
        draw()

        if rules:
            print("I'm the creator of this game, and these are the rules.")
            rules = False
            choice = "> "
        else:
            choice = input("# ")

        if choice == "1":
            clear()
            name = input("# What's your name, hero? ")
            menu = False
            play = True
        elif choice == "2":
            try:
                f = open("load.txt", "r")
                load_list = f.readlines()
                if len(load_list) == 9:
                    name = load_list[0][:-1]
                    HP = int(load_list[1][:-1])
                    ATK = int(load_list[2][:-1])
                    pot = int(load_list[3][:-1])
                    elix = int(load_list[4][:-1])
                    gold = int(load_list[5][:-1])
                    x = int(load_list[6][:-1])
                    y = int(load_list[7][:-1])
                    key = bool(load_list[8][:-1])
                    clear()
                    # print(name, HP, ATK)
                    print(f"Welcome back, {name}!")
                    input("> ")
                    menu = False
                    play = True
                else:
                    print("Corrupt save file!")
                    input("> ")
            except OSError:
                print("No loadable save file!")
                input("> ")
        elif choice == "3":
            rules = True
        elif choice == "4":
            quit()

    while play:
        save()   # autosave
        clear()

        if not standing:
            if biom[map[y][x]]["e"]:
                if random.randint(0, 100) <= 30:
                    fight = True
                    battle()

        if play:
            draw()
            print("LOCATION: " + biom[map[y][x]]["t"])
            draw()
            print(f"NAME: {name}")
            print(f"HP: {HP}/{HPMAX}")
            print(f"ATX: {ATK}")
            print(f"POTIONS: {pot}")
            print(f"ELIXERS: {elix}")
            print(f"GOLD: {gold}")
            print(f"COORD: ({x}, {y})")
            draw()
            print("0 - SAVE AND QUIT")
            if y > 0:
                print("1 - NORTH")
            if x < x_len:
                print("2 - EAST")
            if y < y_len:
                print("3 - SOUTH")
            if x > 0:
                print("4 - WEST")
            if pot > 0:
                print("5 - USE POTION (30HP")
            if elix > 0:
                print("6 - USE ELIXER (50HP")
            draw()

            dest = input("# ")

            if dest == "0":
                play = False
                menu = True
                save()
            elif dest == "1":
                if y > 0:
                    y -= 1
                    standing = False
            elif dest == "2":
                if x < x_len:
                    x += 1
                    standing = False
            elif dest == "3":
                if y < y_len:
                    y += 1
                    standing = False
            elif dest == "4":
                if x > 0:
                    x -= 1
                    standing = False
            elif dest == "5":
                if pot > 0:
                    pot -= 1
                    heal(30)
                else:
                    print("No potions!")
                input("> ")
                standing = True
            elif dest == "6":
                if elix > 0:
                    elix -= 1
                    heal(50)
                else:
                    print("No elixers!")
                input("> ")
                standing = True
            else:
                standing = True
