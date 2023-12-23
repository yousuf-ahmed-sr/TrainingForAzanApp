import random
level2=0
p_max_hp=15
lost=False
p_hp=p_max_hp
e_hp=0
e_max_hp=0
fight_start=True
while True:
    e_max_hp=random.randint(10,p_max_hp+5)
    e_hp=e_max_hp
    def find_ability(ability):
        ability_powers={'ability1':{'damage':[2,6],'name':'punch','damage_per_up':1,'heal':0,'skips':0,'heal_per_up':0},'ability2':{'damage':[1,4],'name':'ice frost','damage_per_up':1,'heal':0,'skips':1,'heal_per_up':0},'ability3':{'damage':[0,0],'name':'bandage','damage_per_up':0,'heal':8,'skips':0,'heal_per_up':2},'ability4':{'damage':[3,3],'name':'lifesteal','damage_per_up':1,'heal':3,'skips':0,'heal_per_up':2}}
        return ability_powers.get(ability,'!')
    if fight_start is True:
        print(f"                                                                 Your enemy's health & max health is {e_hp}")
        for i in range(5):
            print()
        print(f'                                                                     your health & max health is {p_hp}')
        print()
        print(f'                                the abilities are 1. damage:2-6, name:punch, damage per upgrade:1, heal:0, skips:0, heal per upgrade:0')
        print('                                      or 2. damage:1-4, name:ice frost, damage per upgrade:1, heal:0, skips:1, heal per upgrade:0')
        print('                                       or 3. damage:0, name: bandage, damage per upgrade:0, heal:8, skips:0, heal per upgrade:2')
        print('                                       or 4. damage:3, name:lifesteal, damage per upgrade:1, heal:3, skips:0, heal per upgrade:2')
    print()
    def Player_attack_without(used_skill):
        global e_hp
        global p_hp
        user_input=input('                                                                    choose an abilities number:')
        user_input2=f'ability{user_input}'
        ability_contents=find_ability(user_input2)
        if ability_contents == '!':
            print(f'                                                                      {user_input} is an invalid ability')
            Player_attack_without(None)
        else:
            if not user_input == used_skill or used_skill is None:
                heal=0
                damage=ability_contents['damage']
                damage=random.randint(damage[0],damage[1])
                e_hp=e_hp-damage
                print()
                if ability_contents['heal'] > 0:
                    for i in range(0,ability_contents['heal']):
                        if not p_hp == p_max_hp:
                            heal+=1
                if damage > 0:
                    if ability_contents['heal'] > 0:
                        print(f"                                                  you used {ability_contents['name']} ability and it dealt {damage} damage and healed {heal} health")
                    else:
                        print(f"                                                               you used {ability_contents['name']} ability and it dealt {damage} damage")
                else:
                    print(f"                                                               you used {ability_contents['name']} ability and it healed {heal} health")
                print()
                p_hp=min(p_hp+heal,p_max_hp)
                print(f"                                                                     Now enemy's health is {e_hp}")
                for i in range(5):
                    print()
                print(f'                                                                         your health is {p_hp}')
                print()
                if ability_contents['skips'] > 0:
                    for i in range(0,ability_contents['skips']):
                        if ability_contents['skips'] == 1:
                            print(f"                                                                       you skiped {ability_contents['skips']} turn")
                        else:
                            print(f"                                                                       you skiped {ability_contents['skips']} turns")
                            print()
                        Player_attack_without(user_input)
            else:
                print()
                print(f'You already used {user_input2} to skip a turn')
                Player_attack_without(user_input)
    def Enemy_attack_without(used_skill,level):
        global e_hp
        global p_hp
        global lost
        global level2
        enemy_input=random.randint(1,4)
        heal=0
        enemy_input2=f'ability{enemy_input}'
        ability_contents=find_ability(enemy_input2)
        if not enemy_input == used_skill or used_skill is None:
            damage=ability_contents['damage']
            damage=random.randint(damage[0],damage[1])
            damage-=min(5-level,ability_contents['damage'][0])
            p_hp=p_hp-damage
            print()
            if ability_contents['heal'] > 0:
                heal=e_hp
                heal+=max(heal+ability_contents['heal'],e_max_hp)-e_hp
            if damage > 0:
                if ability_contents['heal'] > 0:
                    print(f"                                                  enemy used {ability_contents['name']} ability and it dealt {damage} damage and healed {heal} health")
                else:
                    print(f"                                                               enemy used {ability_contents['name']} ability and it dealt {damage} damage")
            else:
                print(f"                                                               enemy used {ability_contents['name']} ability and it healed {heal} health")
            print()
            e_hp+=heal
            print(f"                                                                     Now enemy's health is {e_hp}")
            for i in range(5):
                print()
            if p_hp > 0:
                print(f'                                                                         your health is {p_hp}')
            else:
                if lost is False:
                    print('                                                                           you lost :(')
                    lost=True
            print()
            if ability_contents['skips'] > 0:
                for i in range(0,ability_contents['skips']):
                    if ability_contents['skips'] == 1:
                        print(f"                                                                       enemy skiped {ability_contents['skips']} turn")
                    else:
                        print(f"                                                                       enemy skiped {ability_contents['skips']} turns")
                        print()
                    Enemy_attack_without(enemy_input,level2)
        else:
            Enemy_attack_without(enemy_input,level2)
    Player_attack_without(None)
    Enemy_attack_without(None,level2)
    fight_start=False
    if not p_hp > 0:
        level2+=1
        break
    else:
        if not e_hp > 0:
            break