# characters
human = 'Humans'
wizard = 'Wizard'
elf = 'Elf'
dragon = 'Drgon'

# health of characters
human_h = 150
wizard_h = 70
elf_h = 100
dragon_h = 300

# damage of characters
human_dmg = 20
elf_dmg = 100
wizard_dmg = 150
dragon_dmg = 50

# Select character 
while True:
    print('1) Human')
    print('2) Wizard')
    print('3) Elf')
    print('4) Dragon')
    character = input('Select Character')
    if character == '1':
        character = human
        char_health = human_h
        char_damage = human_dmg
        print('')
        print('Stat of the Character')
        print('Character Selected is: ' + character)
        print('Health is: ' + str(char_health))
        print('Damages is: ' + str(char_damage))
        print()
        break
