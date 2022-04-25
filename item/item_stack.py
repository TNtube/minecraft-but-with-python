from item.material import Material, MaterialBlock


class ItemStack:
    def __init__(self, material: Material, amount: int):
        self.material = material
        self.size = amount

    def add(self, amount: int):
        self.size += amount
        if self.size > self.material.max_stack_size:
            left_over = self.size - self.material.max_stack_size
            self.size = self.material.max_stack_size
            return left_over
        return 0

    def remove(self):
        self.size -= 1
        if self.size == 0:
            self.material = MaterialBlock.NOTHING

    def __len__(self):
        return self.size
