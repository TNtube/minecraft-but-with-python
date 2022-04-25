import enum
from world.block.block_id import BlockId


class Material:
    class ID(enum.Enum):
        NOTHING = 0
        GRASS = 1
        DIRT = 2
        STONE = 3
        OAK_LOG = 4
        OAK_LEAVES = 5
        SAND = 6
        WATER = 7
        FLOWER = 8

    def __init__(self, material_id: ID, max_stack: int, is_block: bool, name: str):
        self.id: Material.ID = material_id
        self.max_stack_size: int = max_stack
        self.is_block: bool = is_block
        self.name: str = name

    def to_block_id(self):
        return self.id.value

    @classmethod
    def to_material(cls, block_id: BlockId):
        match block_id:
            case BlockId.GRASS:
                return MaterialBlock.GRASS_BLOCK
            case BlockId.DIRT:
                return MaterialBlock.DIRT_BLOCK
            case BlockId.STONE:
                return MaterialBlock.STONE_BLOCK
            case BlockId.OAK_LOG:
                return MaterialBlock.OAK_LOG_BLOCK
            case BlockId.OAK_LEAVES:
                return MaterialBlock.OAK_LEAVES_BLOCK
            case BlockId.SAND:
                return MaterialBlock.SAND_BLOCK
            case BlockId.WATER:
                return MaterialBlock.WATER_BLOCK
            case BlockId.FLOWER:
                return MaterialBlock.FLOWER_BLOCK
            case _:
                return MaterialBlock.NOTHING


class MaterialBlock:
    NOTHING: Material = Material(Material.ID.NOTHING, 64, False, "Nothing")
    GRASS_BLOCK = Material(Material.ID.GRASS, 64, True, "Grass")
    DIRT_BLOCK = Material(Material.ID.DIRT, 64, True, "Dirt")
    STONE_BLOCK = Material(Material.ID.STONE, 64, True, "Stone")
    OAK_LOG_BLOCK = Material(Material.ID.OAK_LOG, 64, True, "Oak Log")
    OAK_LEAVES_BLOCK = Material(Material.ID.OAK_LEAVES, 64, True, "Oak Leaves")
    SAND_BLOCK = Material(Material.ID.SAND, 64, True, "Sand")
    FLOWER_BLOCK = Material(Material.ID.FLOWER, 64, True, "Flower")
    WATER_BLOCK = Material(Material.ID.WATER, 64, True, "Water")
