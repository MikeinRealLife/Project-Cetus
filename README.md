# Project-Cetus
Instructions

run python rogue.py on a unix machine (curses doesn't exist for windows, unfortunately) 
This will launch the game.
Overview
Upon starting the game, the user may choose one of three characters to use during the game. They are the Knight, the Assassin, and the Sorcerer. The Knight hits the hardest and has the most armor, but the lowest intelligence and agility. The Assassin has more health, high agility, but less armor and a slightly weaker attack. The Sorcerer has the highest intelligence and health, some agility but the least armor and attack. 

The player is then placed in the game. The dungeon levels are randomly generated. There are passageways connecting the rooms of the dungeon, but some may be dead ends. This is intentional. The enemies, items, and weapons are all placed randomly throughout the dungeon level. Each level will have a key; this key is required to progress to the next level. As the player progresses through the game killing enemies, they gain experience and will level up, improving their stats. The player may only move in the 4 cardinal directions. The player can get trapped by enemies; it is impossible to move around enemies adjacent to the player. The enemies may also follow the player into the hallways. Somewhere in the dungeon is a special amulet. The player must find this amulet and equip it on the last level of the dungeon to exit and win the game. Note that the player is not able to go backwards in the dungeon...once a flight of stairs in taken, the player is on a new dungeon level and cannot reach the previous levels again. If the amulet required to end the game is missed on a previous level, the game cannot be won. 

The potions do not have a static effect. The higher a character’s intelligence, the greater chance the potion has of being successful, and of having a greater effect. The amulets and food items become stronger the higher the character’s level is.

At any point the player may save the game. However, this is only meant as a way to leave the game and return to the same point. If the player saves the game, the game exits. A series of files containing the saves will be created. The next time the player starts the game, it will prompt the player to choose whether or not to load the previous save. Whichever choice the player makes, that save is then deleted. This prevents the player from being able to revert to a previous save. The player must save every time they wish to be able to return to the game. This ensures permanent death of the player.
Map Key
Enemies are denoted by an uppercase letter
Items, except amulets, are lowercase letters
Amulets are an asterisk, [*]
Cetus Amulet is an ampersand [&]
Weapons are a slash [/]
Stairs are a percent sign [%]
Keys are a tilde [~]
The player is an at sign [@]
Items
Apple: Cures some health
Chicken Leg: Cures more health
Healing Potion: Restores some health
Stamina Potion: Restores some stamina
Espresso: Restores some stamina
Amulet of Knowledge: Increases maximum intelligence while wearing
Amulet of Health: Increases maximum health while wearing
Amulet of Stamina: Increases maximum stamina while wearing
Cetus Amulet: Vibrates with mysterious power
Armor Repair Kit: Fully repairs armor
Weapons
Dagger: increases damage by 0.5 * Weapon Level
Sword: increases damage by 3 * Weapon Level
Axe: increases damage by 1 * Weapon Level
Trident: increases damage by 2 * Weapon Level
Hammer: increases damage by 1.5 * Weapon Level
Controls
WASD, HJKL, or Arrow Keys for movement
Move into enemy for normal attack
[Esc] exits the game from the game screen without saving
[e] Eats Chicken Leg or Apple based on missing health
[c] drinks espresso
[f] uses special attack
[i] opens and closes the inventory/menu
In inventory:
	W/S or UP/DOWN Arrows to move cursor
	[u] equips item next to cursor, [>]
	[i] or [Esc] closes inventory
[d] unequips weapon, if one is equipped
	[a] unequips item, if one is equipped
	[x] saves and quits
Playing the Game
All game files are included in a zip file. Load these files onto the flip server. With all files in the same directory, run “python rogue.py”. This will launch the game. If this is your first time playing, or there are no saves, you will be taken to a launch screen and asked to select your character. If there is a save, you may choose to load it or not. If you load it, it will drop you into the dungeon where you left off. If you do not, you will be asked to choose a character. If you are starting a new game, you will be randomly placed in a randomly generated dungeon level.

Due to the random nature of the game, there is no guarantee what is around. There may be enemies and items in the room; there may be the staircase; there may be the key; there may be any combination of these things. Enemies move when the player moves; they will advance towards you. It is not possible to step around enemies. You can run from them, but if they have you trapped you must fight them! Your special attack [f] will target neighboring enemies, but you must have a weapon equipped and have enough stamina to perform this attack. Enemies can and will follow you into passageways, so you cannot hide from them! Moving over items picks them up. Moving over the stairs when the player has a key goes to the next level. If you have a key, do not step on the stairs until you are ready to go to the next level! 

In the upper lefthand corner is a status window that shows essential stats: health, armor, and stamina. If health runs out, you die. If stamina runs out, you cannot use your special attack. If your armor runs out, you have no more armor. This window also gives updates as to what is happening in the game. It will tell you what items you pick up, what damage you are taking and dealing out, and what enemies you have killed.

This game’s combat implementation is a slight deviation from other roguelike games. While combat is technically turn based, the game does not pause between each turn and you will not need to press a key to advance through messages about the battle. An enemy will strike you whenever it is adjacent to you and you can strike an enemy by running into it. Your character’s agility determines how likely you are to dodge an incoming attack. Enemies also have the ability to dodge attacks. The benefit of our implementation is a quicker, more seamless combat experience. 

Move through the dungeon, finding items and killing enemies. On each level, you must find a key to progress to the next level. Also be sure to look for the special amulet! It will be located somewhere in the dungeon, but is required to win the game. When you reach the final level of the dungeon, the 15th level, there will be a large staircase. To use the stairs and leave the dungeon, thus winning the game, you must be wearing the special amulet and have the final level key. 

You will gain experience (XP) equal to the amount of damage you inflict on enemies you attack. Your character’s level is calculated by XP with the following equation:
	LEVEL = floor(0.25 * sqrt(XP))

When your level increases, so will your health, stamina, and intelligence:
	STAT += floor(sqrt(LEVEL * baseStat))

Enemy health and attack increase with each dungeon level:
	STAT += floor(sqrt(dungeonLevel * baseStat))

Goblins are the strongest and most agile enemies, followed by Skeletons. Arachnids are very weak, but they always appear in groups of three. 

Equipping a weapon allows you to perform the special attack and increases your normal attacks. As you advance through the game, you will find more powerful weapons. When you pick a weapon that is more powerful than the weapon of the same type, it will replace the weaker weapon in your inventory. If the weaker weapon is currently equipped, the game will automatically equip stronger weapon. This means that your inventory will only contain the strongest weapon you have found for each type. 

Amulets add to your character’s abilities. As your level increases, so does the strength of the Amulet’s effect. 

Gameplay Tips
Keep an eye on your health, armor, and stamina in the upper left of the screen. Armor is depleted at a rate of 0.5 per strike from enemy. The more armor you have, the less health you will lose from each enemy attack. Repair your armor and replenish your health as often as you can.
Do not move too quickly through rooms where enemies are present. You can quickly be killed by enemies that chase and catch you if you are not watching your health and armor.
Explore each dungeon fully, even if you have already found the key. There are a limited number of weapons and armor repair kits in the game, so you do not want to miss any. Additionally, the Cetus Amulet, required to exit Level 15, could be on any level. 
You lose Stamina at a rate of 0.0025 per move. Once Stamina, reaches 0, your health will start to decrease at 0.0025 per move.
Special attacks will multiply your attack by 1.5 and target all adjacent enemies, but it will decrease your Stamina by your character’s level. 


