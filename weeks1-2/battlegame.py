# player variable
wizard = 'Wizard'
elf = 'Elf'
human = 'Human'
dragon = 'Dragon'
# player health
wizard_hp = 70
elf_hp = 100
human_hp = 150
dragon_hp = 300
# player damage
wizard_damage = 150
elf_damage = 100
human_damage = 20
dragon_damage = 50
# choose player
while True:
    print('1) Wizard')
    print('2) Elf')
    print('3) Human')
    character = input('Choose your character:')
    opponent = dragon
    if character == '1':
        character = wizard
        my_hp = wizard_hp
        my_damage = wizard_damage
        opponent_hp = dragon_hp
        opponent_damage = dragon_damage
        print('')
        print('GAME STATS')
        print('You have chosen the character: ' + character)
        print('Health: '+ str(my_hp))
        print('Damage: '+ str(my_damage))
        print('')
        print('Your opponent is: ' + opponent)
        print('Health: '+ str(opponent_hp))
        print('Damage: '+ str(opponent_damage))
        break
    elif character == '2':
        character = elf
        my_hp = elf_hp
        my_damage = elf_damage
        opponent_hp = dragon_hp
        opponent_damage = dragon_damage
        print('')
        print('GAME STATS')
        print('You have chosen the character: ' + character)
        print('Health: '+ str(my_hp))
        print('Damage: '+ str(my_damage))
        print('')
        print('Your opponent is: ' + opponent)
        print('Health: '+ str(opponent_hp))
        print('Damage: '+ str(opponent_damage))
        break
    elif character == '3':
        character = human
        my_hp = human_hp
        my_damage = human_damage
        opponent_hp = dragon_hp
        opponent_damage = dragon_damage
        print('')
        print('GAME STATS')
        print('You have chosen the character: ' + character)
        print('Health: '+ str(my_hp))
        print('Damage: '+ str(my_damage))
        print('')
        print('Your opponent is: ' + opponent)
        print('Health: '+ str(opponent_hp))
        print('Damage: '+ str(opponent_damage))
        break
    else:
        print('Unknown character')

# battle with the dragon

while True:
    print('')
    if character == wizard:
        opponent == dragon
        print(character + ' is targeting the ' + opponent + '!')
        print('The ' + character + ' damaged the '  + opponent)
        dragon_hp = dragon_hp - wizard_damage
        print('')
        print('The ' +opponent+ ' hitpoint are now: ' + str(dragon_hp))
        print('')
        print('The '+opponent+ ' strikes back at ' + character)
        wizard_hp = wizard_hp - dragon_damage
        print('The ' +character+ ' hitpoint are now: ' + str(wizard_hp))
        print('')
        print('The ' + character + 'damaged the Dragon!')
        dragon_hp = dragon_hp - wizard_damage
        print('The ' +opponent+' hitpoint are now: ' + str(dragon_hp))
        print('')
        print('The ' +opponent+' has lost the battle')
        print('')
        print("END")
        break
    elif character == elf:
        opponent == dragon
        print(character + ' is targeting the ' + opponent + '!')
        print('The ' + character + ' damaged the '  + opponent)
        dragon_hp = dragon_hp - elf_damage
        print('The ' + opponent+ ' hitpoint are now: ' + str(dragon_hp))
        print('')
        print('The ' + opponent + ' strikes back at ' + character)
        elf_hp = elf_hp - dragon_damage
        print('The ' + character + ' hitpoint are now: ' + str(elf_hp))
        print('')
        print('The ' + character + ' damaged the ' + opponent + '!')
        dragon_hp = dragon_hp - elf_damage
        print('The ' + opponent+ ' hitpoint are now: ' + str(dragon_hp))
        print('')
        print('The ' + opponent+ ' strikes back at ' + character)
        elf_hp = elf_hp - dragon_damage
        print('The '+ character + ' hitpoints are now: ' + str(elf_hp))
        print('')
        print('The ' +character+' has lost the battle')
        print('')
        print("END")
        break
    else: 
        character == human
        opponent == dragon
        print(character + ' is targeting the ' + opponent + '!')
        print('The ' + character + ' damaged the '  + opponent)
        dragon_hp = dragon_hp - human_damage
        print('The ' + opponent+ ' hitpoint are now: ' + str(dragon_hp))
        print('')
        print('The ' + opponent + ' strikes back at ' + character)
        human_hp = human_hp - dragon_damage
        print('The ' + character + ' hitpoint are now: ' + str(human_hp))
        print('')
        print('The ' + character + ' damaged the ' + opponent + '!')
        dragon_hp = dragon_hp - human_damage
        print('The ' + opponent+ ' hitpoint are now: ' + str(dragon_hp))
        print('')
        print('The ' + opponent+ ' strikes back at ' + character)
        human_hp = human_hp - dragon_damage
        print('The '+ character + ' hitpoints are now: ' + str(human_hp))
        print('')
        print('The ' + opponent + ' strikes back at ' + character)
        human_hp = human_hp - dragon_damage
        print('The ' + character + ' hitpoint are now: ' + str(human_hp))
        print('')
        print('The ' +character+' has lost the battle')
        print('')
        print("END")
        break