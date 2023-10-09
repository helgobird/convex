class Data:
    """
    Класс Data содержит в себе две
    точки из условия задачи
    """

    FIRST_POINT = None
    SECOND_POINT = None

    @classmethod
    def set_points(cls, first_point, second_point):
        if not cls.FIRST_POINT:
            cls.FIRST_POINT = first_point
            cls.SECOND_POINT = second_point
