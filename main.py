import random
from typing import List, Tuple
from rooms.rooms import Room


class Game:
    def __init__(self):
        self.health = 100
        self.inventory = {}
        self.room = Room()
        self.initial_player_attack = 5
        self.golden_key_coordinates = None

    def create_map(self, size:int) -> List[List[str]]:
        """
        This function will create the game map, a square matrix fixed by size columns and size rows
        :param size: integer
        :return: Square matrix with the rooms
        """
        if size > 10 or size < 3:
            raise ValueError("Size must be between 3 and 10")
        matrix = [['R' for _ in range(size)] for _ in range(size)]
        return matrix

    def print_map(self,matrix) -> None:
        """
        This method will print the game map
        :param matrix:
        :return: None
        """
        for row in matrix:
            print(row)
        print(f'Health: {self.health}')

    def put_player_on_random_position(self, matrix) -> Tuple[int, int]:
        """
        This method will put the player on the random position of the martix, by taking the size of the matrix
        :param matrix:
        :return: The matrix with player on the random position, marked by "P"
        """
        size = len(matrix)
        random_player_coordinates = (random.randint(0, size - 1), random.randint(0, size - 1))

        return random_player_coordinates

    def _put_golden_key_on_map(self, matrix) -> tuple[int, int ]:
        """
        This method will generate random position for the golden key on the map, by taking the size of the matrix
        If the taken position is marked by "P" - player, the method will regenerate the coordinates for the golden key
        The coordinates will not be visible by the player.
        :param matrix:
        :return: tuple with the golden key coordinates
        """
        size = len(matrix)
        gk_x = random.randint(0, size - 1)
        gk_y = random.randint(0, size - 1)
        while matrix[gk_x][gk_y] == 'P':
            gk_x = random.randint(0, size - 1)
            gk_y = random.randint(0, size - 1)
        return gk_x,gk_y

    def choose_prompt(self, msg: str, choices: List[str]):
        """Ask until a valid choice (case-insensitive) is entered."""
        valid = [c.lower() for c in choices]
        while True:
            choice = input(msg).strip().lower()
            if choice in valid:
                return choice
            print(f'Invalid choice!\nValid choices: {", ".join(valid)}')

    def equip_item(self, item_stats: dict[str, int]):
        """
        Thi method gets the attack power from the item_stats dictionary and the new attack power of the player
        is increased by summing the item_stats['attack'] + the initial player power
        :param item_stats: dictionary with item statistics
        :return: the increased attack power of the player
        """
        current_attack_power = self.initial_player_attack + item_stats['attack']
        return current_attack_power


    def save_item_in_inventory(self, item_name: str)-> None:
        """
        This method will store the item in the inventory of the player
        :param item_name:
        :return: Nothing is returned
        """
        if item_name not in self.inventory:
            self.inventory[item_name] = 0
        self.inventory[item_name] += 1


    def _moves(self) -> dict[str, tuple[int, int]]:
        """
        This method will map the direction of the player
        :return: dictionary with coordinates
        """
        return {"u": (-1, 0), "d": (1, 0), "l": (0, -1), "r": (0, 1)}

    def _ask_direction(self) -> str:
        """
        This method will ask the player to enter the direction to move
        :return:
        """
        return self.choose_prompt(
            "Enter direction to move.\n [u] - Up, [d] - Down, [l] - Left, [r] - Right: ",
            choices=["u", "d", "l", "r"]
        ).lower()

    def _in_bounds(self, r: int, c: int, n: int) -> bool:
        """
        This method will check if a coordinate is within the bounds of the map
        :param r: row
        :param c: col
        :param n: size of the matrix
        :return: true/false
        """
        return 0 <= r < n and 0 <= c < n

    def _next_position(self, row_index: int, col_index: int, direction: str) -> tuple[int, int]:
        """
        This method will calculate the next position of the player
        :param row_index: row-index
        :param col_index: col-index
        :param direction: u/d/l/r
        :return: updated new player coordinates
        """
        drow, dcol = self._moves()[direction]
        return row_index + drow, col_index + dcol

    # Map Updates
    def _place_player(self, matrix: list[list[str]], from_pos: tuple[int, int], to_pos: tuple[int, int]) -> None:
        """
        This method will place the player on the map
        :param matrix: the actual game map
        :param from_pos: from position
        :param to_pos: to position
        :return: Nothing is returned
        """
        from_row, from_col = from_pos
        to_row, to_col = to_pos
        matrix[from_row][from_col] = 'X'
        matrix[to_row][to_col] = 'P'

    def _handle_revisited(self, matrix: list[list[str]], row: int, col: int, new_row: int, new_col: int) -> tuple[int, int] :
        """
        This method will check if the player has already been in the current room
        :param matrix: the actual game map
        :param row: row
        :param col: col
        :param new_row: new row
        :param new_col: new col
        :return: the new player coordinates
        """
        print('You have already been in this room! You will get no reward.')
        self._place_player(matrix, (row, col), (new_row, new_col))
        self.print_map(matrix)
        return new_row, new_col

    # Room entry effects (loot + monster reveal)
    def _enter_room_and_apply_effects(self) -> bool:
        """
        This method will create a room, increase the player's attack power and save the found item inside the inventory
        :return: Nothing is returned, only printed
        """
        entered_room, room_description, item_in_room, item_stats, monster, monster_stats = self.room.generate_room()
        print(f'{"#" * 20} You have entered: {entered_room} {"#" * 20}')
        print(room_description)
        # Item
        print(f'You found {item_in_room} with +{item_stats["attack"]} attack power')
        new_player_attack = self.equip_item(item_stats)
        self.save_item_in_inventory(item_in_room)
        print(
            f'You equipped {item_in_room} with +{item_stats["attack"]} attack.\nYour new attack power is: {new_player_attack}')

        # Monster
        print(f'{monster} with {monster_stats["health"]} HP and {monster_stats["attack"]} ATK awaits to fight it.\n')

        if not self._fight_monster(monster_stats, new_player_attack):
            return False
        return True

    def create_room(self):
        """
        This method uses the Room class to create a random room.
        :return: object of Room class
        """
        return self.room.generate_room()

    def _decrease_health(self, decrease_amount: int) -> None:
        self.health -= decrease_amount

    def _check_if_player_is_still_alive(self) -> bool:
        if self.health <= 0:
            return False
        return True



    def _fight_monster(self, monster_stats: dict[str, int], current_player_attack_power: int) -> bool:
        monster_health = monster_stats["health"]
        monster_attack = monster_stats["attack"]
        battle_queue = ['player','monster']
        while monster_health > 0:
            if battle_queue[0] == 'player':
                monster_health -= current_player_attack_power
                player = battle_queue.pop(0)
                battle_queue.append(player)
            else:
                self._decrease_health(monster_attack)
                monster = battle_queue.pop(0)
                battle_queue.append(monster)
                if not (self._check_if_player_is_still_alive()):
                    return False
        return True





    def _golden_key_is_found(self, current_player_coordinates: tuple[int, int]) -> bool:
        """
        This method will check if the player has found the golden key by comparing the coordinates
        :param current_player_coordinates:  current player position on the map
        :return: true/false
        """
        return current_player_coordinates == self.golden_key_coordinates

    def move_player(self, current_player_coordinates: tuple[int, int], matrix: List[list[str]]) -> List[list[str]] | str:
        """
        This method will handle the player movement on the game map
        :param current_player_coordinates: the position of the player on the map
        :param matrix: the current game map
        :return: the updated game map after player movement
        """
        grid_size = len(matrix)
        row_index, col_index = current_player_coordinates

        while self.health > 0:
            direction = self._ask_direction()
            new_row_index, new_col_index = self._next_position(row_index, col_index, direction)

            # Bounds check
            if not self._in_bounds(new_row_index, new_col_index, grid_size):
                print("You can't move outside the map!\n")
                self.print_map(matrix)
                print()
                continue

            # Revisited tile
            if matrix[new_row_index][new_col_index] == 'X':
                row_index, col_index = self._handle_revisited(
                    matrix, row_index, col_index, new_row_index, new_col_index
                )

                continue





            # Fresh room: place player, THEN update internal coords (this was missing)
            self._place_player(matrix, (row_index, col_index), (new_row_index, new_col_index))
            row_index, col_index = new_row_index, new_col_index

            # Check if golden key is found
            if self._golden_key_is_found((row_index, col_index)):
                matrix[row_index][col_index] = 'G'
                print('You have found the golden key!')
                print('You have won the game!')
                break

            if self._enter_room_and_apply_effects():
                self.print_map(matrix)
                print(f'Your current inventory is: {self.inventory}')
            else:
                return f"The monster defeated you! Game over!"


        return matrix




    def main_loop(self):
        """
        This method will run the main loop of the game
        :return:
        """
        game_map = self.create_map(3)
        player_x, player_y = self.put_player_on_random_position(game_map)
        game_map[player_x][player_y] = 'P'
        self.golden_key_coordinates = self._put_golden_key_on_map(game_map)
        self.print_map(game_map)

        updated_game_map = self.move_player((player_x, player_y), game_map)
        self.print_map(updated_game_map)







if __name__ == '__main__':
    game = Game()
    game.main_loop()