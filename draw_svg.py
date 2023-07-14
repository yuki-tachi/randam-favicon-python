import generate_pattern
from dataclasses import dataclass
from typing import Protocol

DIVISION = 5
FILL = "#B30F3A"
BASE_SIZE = 128

class Drawable(Protocol):
    def set_size(self, division:int) -> None:
        ...
    def set_pos(self, pos_x:int|float, pos_y:int|float) -> None:
        ...
    def draw_svg(self) -> str:
        ...

@dataclass
class Rect():
    size: int | float = 0
    # x,yは配置場所の位置を想定していて、実際の配置はx * sizeになる
    x: int | float = 0
    y: int | float = 0
    # 16進数のカラーコード
    fill: str = "#B30F3A"
    def set_size(self, division) -> None:
        self.size=round(BASE_SIZE / division)

    def set_pos(self, pos_x, pos_y) -> None:
        self.x = pos_x
        self.y = pos_y

    def draw_svg(self) -> str:
        return f'<rect x="{round(self.x * self.size, 2)}" y="{round(self.y * self.size, 2)}" width="{self.size}" height="{self.size}" fill="{self.fill}"/>\n'

@dataclass
class Circle():
    size: int | float = 0
    # x,yは配置場所の位置を想定していて、実際の配置はx * sizeになる
    x: int | float = 0
    y: int | float = 0
    # 16進数のカラーコード
    fill: str = "#B30F3A"
    def set_size(self, division) -> None:
        self.size=round(BASE_SIZE / division)

    def set_pos(self, pos_x, pos_y) -> None:
        self.x = pos_x
        self.y = pos_y
        
    def draw_svg(self) -> str:
        return f'<circle cx="{round(self.x * self.size + self.size / 2, 2)}" cy="{round(self.y * self.size + self.size / 2, 2)}" r="{round(self.size / 2 - 1, 2)}" fill="{self.fill}"/>\n'

@dataclass
class Triangle():
    size: int | float = 0
    # x,yは配置場所の位置を想定していて、実際の配置はx*sizeになる
    x: int | float = 0
    y: int | float = 0
    # 16進数のカラーコード
    fill: str = "#B30F3A"
    def set_size(self, division) -> None:
        self.size=round(BASE_SIZE / division)
    
    def set_pos(self, pos_x, pos_y) -> None:
        self.x = pos_x
        self.y = pos_y

    def draw_svg(self) -> str:
        x1 = round(self.x*self.size, 2)
        y1 = round(self.y*self.size+self.size, 2)
        x2 = round(self.x*self.size+self.size/2, 2)
        y2 = round(self.size*self.y + self.size-self.size/2*1.73, 2)
        x3 = round(self.x*self.size+self.size, 2)
        y3 = round(self.y*self.size+self.size, 2)
        return f'<polygon points="{x1},{y1} {x2},{y2} {x3},{y3}" fill="{self.fill}"/>\n'

def create_svg(svg_str: str):
    with open("favicon.svg", "w") as f:
        f.write('<?xml version="1.0" encoding="UTF-8" ?>\n')
        f.write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {BASE_SIZE} {BASE_SIZE}">\n')
        f.write(svg_str)
        f.write('</svg>')

def get_draw_svg(shape:Drawable, pattern:list[list[bool]]) -> str:
    svg_str = ""
    for row_i, row in enumerate(pattern):
        for col_i, col in enumerate(row):
            if col:
                shape.set_pos(col_i, row_i)
                svg_str += shape.draw_svg()
    return svg_str

# 直接呼び出して生成
# shpae = Triangle(fill=FILL)
# shpae.set_size(DIVISION)
# pattern = generate_pattern.execute(DIVISION)
# svg = get_draw_svg(shpae, pattern)
# create_svg(svg)