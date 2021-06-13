
def main():
    x, y = 300, 400
    width, height = 200, 300

    draw_house(x, y, width, height)


def draw_house(x, y, width, height):
    """
        Нарисовать домик ширыны width и height от опорной точки (x, y),
        которая находится в середине нижней точки фундамента.
        :param x: координата х середины домика
        :param y: координата у низа фундамента
        :param width: полная ширина домика(фундамент или вылеты крыши включены)
        :param height: полная высота домика
        :return: None
        """
    print('типа рисую домик', x, y, width, height)
    foundation_height = 0.05 * height
    walls_width = 0.9 * width
    walls_height = 0.5 * height
    roof_height = height - foundation_height - walls_height

    draw_house_foundation(x, y, width, foundation_height)
    draw_house_walls(x, y - foundation_height, walls_width, walls_height)
    draw_house_roof(x, y - foundation_height - walls_height, width, roof_height)


def draw_house_foundation(x, y, width, height):
    """
    Нарисовать основание домика ширыны width и height от опорной точки (x, y),
    которая находится в середине нижней точки фундамента.
    :param x: координата х середины фундамента
    :param y: координата у низа фундамента
    :param width: полная ширина фундамента
    :param height: полная высота фундамента
    :return: None
    """
    print('типа рисую основание ', x, y, width, height)
    pass


def draw_house_walls(x, y, width, height):
    print('типа рисую стены', x, y, width, height)
    pass


def draw_house_roof(x, y, width, height):
    print('типа рисую крышу...', x, y, width, height)
    pass


main()

