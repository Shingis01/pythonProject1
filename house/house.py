
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
    print('tipa risyu', x, y, width, height)
    pass # do nothing


x, y = 100, 100
width, height = 200, 200

draw_house(x, y, width, height) # modified
