from enum import IntEnum


class CollisionChannel(IntEnum):
    Player = 0,
    Enemy = 1,
    Entity = 2,
    World = 3
    EnemyObstacle = 4
