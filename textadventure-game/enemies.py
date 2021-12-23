class Enemy:
    def __init__(self, name, hp, damage, experience):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.experience = experience

    def is_alive(self):
        return self.hp > 0


class Titan(Enemy):
    def __init__(self):
        super().__init__(name="Titan", hp=30, damage=40, experience=40)


class Knowhere(Enemy):
    def __init__(self):
        super().__init__(name="Knowhere", hp=15, damage=10, experience=15)


class Vormir(Enemy):
    def __init__(self):
        super().__init__(name="Vormir", hp=18, damage=15, experience=10)


class Zen(Enemy):
    def __init__(self):
        super().__init__(name="Zen", hp=20, damage=20, experience=12)


class Nidavellir(Enemy):
    def __init__(self):
        super().__init__(name="Nidavellir", hp=10, damage=10, experience=20)

class Missile(Enemy):
    def __init__(self):
        super().__init__(name="Missile", hp=15, damage=10, experience=20)

class Muller(Enemy):
    def __init__(self):
        super().__init__(name="Muller", hp=20, damage=20, experience=20)

