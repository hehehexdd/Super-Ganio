from enum import IntEnum


class CollisionAction(IntEnum):
    Block = 0,
    Pass = 1


class CollisionChannel(IntEnum):
    Entity = 1,
    World = 2,
    EnemyObstacle = 3,
    Objective = 4,
    Damage = 5,
    Death = 6
