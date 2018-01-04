

game_weapons = {'Staff': ['Well it\'s better than a large stick', 1],
               'Dagger': ['Small stabby knife', 1],
               'Sword': ['Sword', 2],
               'Large Stick': ['Too bad it\'s not a real staff', 0.5],
               'Axe': ['And my axe!', 1],
               'Trident': ['Hello Poseidon', 2],
               'Club': ['Beat \'em up!', 2],
               'Sickle': ['Slashing!', 2],
               'Hammer': ['Not quite Thor\'s', 2]}

def get_description(weapon):
    return game_weapons.get(weapon, None)

def take_weapon(name, weapon, description, damage, player):
    if weapon in game_weapons:
        if weapon in player.items_inv:
            player.items_inv[name] += 1
        else:
            player.items_inv[name] = list()
            player.items_inv[name].append(weapon)
            player.items_inv[name].append(description)
            player.items_inv[name].append(damage)

        return True
    else:
        return False

def remove_weapon(weapon, player):
    if player.items_inv.get(weapon, None) == 1:
        del player.items_inv[weapon]
    else:
        player.items_inv[weapon] -= 1
    return

def chooseWeapon(weapon, damage, player):
    print(weapon)
    print(damage)
    if weapon == 'Staff':
        equipWeapon(1 * damage, player)
    elif weapon == 'Dagger':
        equipWeapon(1 * damage, player)
    elif weapon == 'Sword':
        equipWeapon(2 * damage, player)
    elif weapon == 'Large Stick':
        equipWeapon(0.5 * damage, player)
    elif weapon == 'Axe':
        equipWeapon(1 * damage, player)
    elif weapon == 'Trident':
        equipWeapon(2 * damage, player)
    elif weapon == 'Club':
        equipWeapon(2 * damage, player)
    elif weapon == 'Sickle':
        equipWeapon(2 * damage, player)
    elif weapon == '':
        equipWeapon(0, player)
    elif weapon == 'Hammer':
        equipWeapon(2 * damage, player)
    return

def equipWeapon(weapon, damage, player):
    player.addedAttack = damage
    if weapon != '':
        player.weapon_equipped = weapon
    else:
        player.weapon_equipped = None

def unequipWeapon(player):
    player.addedAttack = 0
    player.weapon_equipped = None
