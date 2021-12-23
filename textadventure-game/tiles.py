import items
import enemies
import actions
import world
import player
#import sounds


class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError()

    def modify_player(self, player):
        raise NotImplementedError()

    def adjacent_moves(self):
        """Returns all move actions for adjacent tiles."""
        moves = []
        if world.tile_exists(self.x + 1, self.y):
            moves.append(actions.MoveEast())
        if world.tile_exists(self.x - 1, self.y):
            moves.append(actions.MoveWest())
        if world.tile_exists(self.x, self.y - 1):
            moves.append(actions.MoveNorth())
        if world.tile_exists(self.x, self.y + 1):
            moves.append(actions.MoveSouth())
        return moves

    def available_actions(self):
        """Returns all of the available actions in this room."""
        moves = self.adjacent_moves()
        moves.append(actions.ViewInventory())
        moves.append(actions.Equip())
        moves.append(actions.Heal())
        moves.append(actions.Status())

        return moves


class Space(MapTile):
    # override the intro_text method in the superclass
    def intro_text(self):
        return """
      
░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗  ████████╗░█████╗░
░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝  ╚══██╔══╝██╔══██╗
░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░  ░░░██║░░░██║░░██║
░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░  ░░░██║░░░██║░░██║
░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗  ░░░██║░░░╚█████╔╝
░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝  ░░░╚═╝░░░░╚════╝░

░██████╗██████╗░░█████╗░░█████╗░███████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝
╚█████╗░██████╔╝███████║██║░░╚═╝█████╗░░
░╚═══██╗██╔═══╝░██╔══██║██║░░██╗██╔══╝░░
██████╔╝██║░░░░░██║░░██║╚█████╔╝███████╗
╚═════╝░╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚══════╝ 
        
        
        Welcome to the Space. Space has planets with their enemy. All the plaents are causing harm to the 
        mother planet. The enemy tries to kill the player and doesn not allow to enter the planet and reach 
        destination. this is the space with planets : Vomir, Titan, Zen, Nadevillr. In order to reach the 
        destination travel all the planets and destroy the enemy. 
        """

    def modify_player(self, player):
        # Room has no action on player
        return player.lockpass()


class LootRoom(MapTile):
    def __init__(self, x, y, item):
        self.item = item
        super().__init__(x, y)

    def add_loot(self, player):
        player.inventory.append(self.item)

    def modify_player(self, player):
        self.add_loot(player)


class EnemyRoom(MapTile):
    def __init__(self, x, y, enemy):
        self.enemy = enemy
        super().__init__(x, y)

    def modify_player(self, the_player):
        if self.enemy.is_alive():
            the_player.hp = the_player.hp - self.enemy.damage
            print("Enemy does {} damage. You have {} HP remaining.".format(
                self.enemy.damage, the_player.hp))

    def available_actions(self):
        if self.enemy.is_alive():
            return [actions.Flee(tile=self), actions.Attack(enemy=self.enemy)]
        else:
    
            return self.adjacent_moves()


class EmptySpace(MapTile):
    def intro_text(self):
        return """
        An unremarkable space. You must forge onwards.
        """

    def modify_player(self, player):
        # Room has no action on player
        pass


class TitanPlanet(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Titan())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            A Titan in front of you!
            """
        else:
            return """
            The titan disappers in the space and is lost forever!.
            """


class ZenPlanet(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Zen())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
             A Zen jumps down in front of you!
             """
        else:
            return """
             The Zen disappers in the space and is lost forever!.
             """


class FindDaggerRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Dagger())

    def intro_text(self):
        return """
        Your notice something shiny in the corner.
        It's a dagger! You pick it up.
        """


class Earthile(MapTile):
    def intro_text(self):
        return """
        You see a bright light in the distance...
        ... it grows as you get closer! It's sunlight!
 
 
        Victory is yours!
        """

    def modify_player(self, player):
        player.victory = True


class NidavellirPalent(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Nidavellir())

    def intro_text(self):
        if self.enemy.is_alive():
            
            return """
             A giant Nidavellir is coming to attack you.
             """
        else:
            return """
             Hurray! you have knocked down Nidavellir
             """


class MissilePlanet(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Missile())

    def intro_text(self):
        if self.enemy.is_alive():
            
            return """
             Missile Planets Enemy Attcks You
             """
        else:
            return """
             you have escaped from the Attack!.
             """


class MissielPlanet(EnemyRoom):
    def __init__(self, x, y, ):
        super().__init__(x, y, enemies.Missile())

    def intro_text(self):
        if self.enemy.is_alive():
            return """ You have eneterd the planet and had you have been attacked by the enemy"""
        else:
            return """finished.lets keep going!"""


class space2(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Nidavellir())

    def intro_text(self):
        return """
        You have eneterd space2, Space2 has enimies and newly formed planets. Enemy attacks when you enter
        the planet
        """


class Enamulate(MapTile):
    def intro_text(self):
        return """
        You have entered Planet Eanmulate, It is the planet with enemy far away from other planets 
        in the space. It is the new formed planet and has inhabited with enemy 
        and The enemy attcks you when you have entered the planet.
        The planet has the water, planets and condition to live on. To safegaurd the planet and use the 
        resources for future kill the enemy and save the planet.
        """

    def modify_player(self, player):
        # Room has no action on player
        pass




'''class Grain(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.SnakeMutts())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            District 9 specializes in producing grain and salts.
            It is the least mentioned district in the series; no named character from the district has appeared in the series
            """
        else:
            return """
            killed"""

'''
class Maso(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Titan())

    def intro_text(self):
        return """** Titan is one of the most powerful weapons.Well done***
"
        """


class Luxury(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Vormir)

    def intro_text(self):
        return """
        Welcome to the space-2, It has the enimies with newly formed planets
        """


class Transition(MapTile):

    def intro_text(self):
        return """

░█████╗░░█████╗░███╗░░██╗░██████╗░██████╗░░█████╗░████████╗░██████╗██╗
██╔══██╗██╔══██╗████╗░██║██╔════╝░██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██║
██║░░╚═╝██║░░██║██╔██╗██║██║░░██╗░██████╔╝███████║░░░██║░░░╚█████╗░██║
██║░░██╗██║░░██║██║╚████║██║░░╚██╗██╔══██╗██╔══██║░░░██║░░░░╚═══██╗╚═╝
╚█████╔╝╚█████╔╝██║░╚███║╚██████╔╝██║░░██║██║░░██║░░░██║░░░██████╔╝██╗
░╚════╝░░╚════╝░╚═╝░░╚══╝░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═════╝░╚═╝
        
        """

    def modify_player(self, player):
        # Room has no action on player

        return player.level_up()


class NuclearPower(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Jabberjay())

    def intro_text(self):
        if self.enemy.is_alive():
            return """ Jabberjay are powerful. You need to use everything to beat him***
            Before the Dark Days war, District 13 specialized in nuclear technology and the development of emerging technologies for use by Panem's military.
            """
        else:
            return """$$$$ you have defeated president snows challenge $$$"""


class Transportation(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Titan())

    def intro_text(self):
        if self.enemy.is_alive():
            return """You have encountered Titan
            Space-2 is the space with newly formed planets and enemies
            """
        else:
            return """We are almost there!Dont give up"""


