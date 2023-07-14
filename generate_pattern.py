import math
import random

def execute(division: int) -> list[list[bool]]:
    if division <= 0:
        raise Exception('invaild division')

    mirror_matrix = [[False] * division for i in range(division)]
    center = int(division / 2 if division % 2 == 0 else math.floor(division / 2 + 1))

    for row in range(division):
        for col in range(center):
            mirror_matrix[row][col] =  mirror_matrix[row][(division - 1) - col] = random.choice([True,False])
    # print(mirror_matrix)
    return mirror_matrix

# execute(5)