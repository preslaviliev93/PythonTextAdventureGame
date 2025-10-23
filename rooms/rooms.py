import random
from typing import Dict, Tuple


class Room:

    def monsters_in_room(self) -> Tuple[str, Dict[str, int]]:
        monsters = {
            "Small Goblin": {"health": 5, "attack": 2},
            "Ghoul": {"health": 8, "attack": 3},
            "Vampire Bats": {"health":1, "attack": 0},
            "Poisonous Snake": {"health": 10, "attack": 10},
            "Angry Ghost": {"health":1, "attack": 4 },
            "Bear": {"health": 30, "attack": 35},
            "Small Demon": {"health": 14, "attack": 8},
            "Medium Demon": {"health": 25, "attack": 20},
            "Large Demon": {"health": 50, "attack": 45},
            "Skeleton Warrior": {"health": 12, "attack": 6},
            "Wild Boar": {"health": 18, "attack": 9},
            "Bandit": {"health": 16, "attack": 7},
            "Troll": {"health": 40, "attack": 18},
            "Ogre": {"health": 55, "attack": 22},
            "Swamp Hag": {"health": 20, "attack": 12},
            "Cave Spider": {"health": 6, "attack": 5},
            "Dire Wolf": {"health": 22, "attack": 14},
            "Shade Stalker": {"health": 15, "attack": 16},
            "Mad Alchemist": {"health": 14, "attack": 10},
            "Stone Golem": {"health": 70, "attack": 25},
            "Feral Cultist": {"health": 24, "attack": 13},
            "Harpy": {"health": 12, "attack": 9},
            "Sand Wraith": {"health": 28, "attack": 17},
            "Mimic Chest": {"health": 26, "attack": 19},
            "Frost Elemental": {"health": 32, "attack": 21},
            "Fire Imp": {"health": 9, "attack": 11},
            "Cursed Knight": {"health": 45, "attack": 28},
            "Basilisk": {"health": 38, "attack": 24},
            "Necromancer": {"health": 30, "attack": 27},
            "Rotting Colossus": {"health": 90, "attack": 33},
            "Thunder Drake": {"health": 60, "attack": 30},
            "Abyssal Horror": {"health": 85, "attack": 42},
            "Crystal Scorpion": {"health": 34, "attack": 20},
            "Forest Ent": {"health": 75, "attack": 26},
            "Plague Rat Swarm": {"health": 10, "attack": 8},
            "Arcane Sentinel": {"health": 50, "attack": 32},
            "Blood Revenant": {"health": 28, "attack": 23},
        }
        monster_name, stats = random.choice(list(monsters.items()))
        return monster_name, stats

    def items_in_room(self) -> Tuple[str, Dict[str, int]]:
        items = {
            "Knife": {"attack": 5},
            "Bat": {"attack": 2},
            "Shovel": {"attack": 2},
            "Toaster": {"attack": 20},
            "Trebuchet": {"attack": 50},
            "Compound Bow": {"attack": 25},
            "Rifle": {"attack": 30},
            "Machine Gun": {"attack": 40},
            "A gulp of air": {"attack": 0},
            "Rusty Dagger": {"attack": 3},
            "Short Sword": {"attack": 7},
            "Longsword": {"attack": 12},
            "War Hammer": {"attack": 15},
            "Battle Axe": {"attack": 18},
            "Spear": {"attack": 9},
            "Crossbow": {"attack": 14},
            "Blunderbuss": {"attack": 22},
            "Molotov Cocktail": {"attack": 16},
            "Throwing Knives": {"attack": 8},
            "Spiked Club": {"attack": 11},
            "Enchanted Wand": {"attack": 13},
            "Runic Staff": {"attack": 19},
            "Crystal Blade": {"attack": 26},
            "Thunder Mace": {"attack": 28},
            "Frostbrand": {"attack": 24},
            "Flamethrower": {"attack": 35},
            "Chainsaw": {"attack": 33},
            "Dragonbone Bow": {"attack": 29},
            "Orb of Impact": {"attack": 21},
            "Quiver of Piercing Arrows": {"attack": 10},
            "Heavy Shield Bash": {"attack": 6},
            "Spartan Kopis": {"attack": 17},
            "Meteor Hammer": {"attack": 23},
            "Witch’s Broom (Whack!)": {"attack": 4},
            "Pocket Anvil": {"attack": 20},
            "Pan of Justice": {"attack": 9},

        }
        item_name, item_stats = random.choice(list(items.items()))
        return item_name, item_stats


    def room_descriptions(self):
        descriptions = {
            "Dungeon": "You enter dark and moisty dungeon. Beware of the "
                       "dangers, lurking in the shadows",
            "Garden": "Before you stands a garden, full of roses. The smell is great. You get a calming feeling that "
                      "this room wont hold any dangers...",
            "The Attic": "Dusty and unpleasant, but you know that there might be something valuable hidden there. ",
            "Maze": "You find yourself inside a maze. Beware of the dangers hidden on your way out of it.",
            "Temple": "You hear strange noises, your body shivers, but you keep your courage and continue on your quest "
                      "to find the golden key.",
            "Library of Whispers": "Shelves groan with forbidden tomes; pages flutter without wind.",
            "Crystal Cavern": "Walls glitter with prisms that split your torchlight into rainbows.",
            "Abandoned Mine": "Old rails and broken carts; the air tastes of iron and dust.",
            "Ancient Crypt": "Names worn smooth on stone; a chill seeps into your bones.",
            "Blacksmith’s Forge": "Cold anvils and scattered tools; soot footprints lead deeper.",
            "Flooded Tunnels": "Knee-deep water muffles steps; ripples betray unseen things.",
            "Observatory": "A cracked lens gazes at a starless sky; gears tick out of sync.",
            "Clockwork Hall": "Pistons hiss and cogs bite; an errant gear spins on the floor.",
            "Market Ruins": "Toppled stalls and coin litter; a breeze rings a lonely bell.",
            "Sunken Shrine": "Coral claims old idols; bubbles whisper from below.",
            "Bandit Camp": "Doused embers and torn flags; loot sacks lie half-buried.",
            "Witch’s Hut": "Bundles of herbs and jars of eyes; the kettle is still warm.",
            "Glacial Pass": "Wind flays your cheeks; ice groans beneath your boots.",
            "Mushroom Grove": "Bioluminescent caps pulse; spores dance in your torchlight.",
            "Spider Nest": "Silk veils everything; husks stare with empty sockets.",
            "Forgotten Theater": "Red curtains hang in tatters; the stage creaks underfoot.",
            "Thorn Maze": "Barbs snag your cloak; the path closes behind you.",
            "Hall of Mirrors": "Reflections multiply; some don’t copy your moves.",
            "Golem Foundry": "Molten rivulets cool in trays; molds wait for a spark of life.",
            "Cursed Orchard": "Fruit gleams like gems; branches bend toward you.",
            "Bone Pit": "White shards crunch; something tunnels just out of sight.",
            "Arcane Laboratory": "Ritual circles glow faintly; notes end mid-sentence.",
            "Beacon Tower": "A dead lantern looms; the sea roars far below.",
        }
        room_name, room_description = random.choice(list(descriptions.items()))
        return room_name, room_description

    def generate_room(self):
        current_room, room_desc = self.room_descriptions()
        item, item_stat = self.items_in_room()
        current_monster, monster_stat = self.monsters_in_room()

        return current_room, room_desc, item, item_stat, current_monster, monster_stat

    def main(self):
        r, r_desc, item, item_stat,current_monster, monster_stat = self.generate_room()
        print(f"{'#' * 20} {r} {'#' * 20}\n{r_desc}")
        print(f"{item} - {item_stat}")
        print(f"{current_monster} - {monster_stat}")


