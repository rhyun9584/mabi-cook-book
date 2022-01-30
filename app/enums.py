from enum import Enum, auto


class Method(Enum):
    """
    cook 모델에 들어갈 cooking method enum
    """
    MIXING = '혼합',
    BAKING = '굽기',
    SIMMERING = '삶기',
    KNEADING = '반죽',
    BOILING = '끓이기',
    NOODLE = '면 만들기',
    DEEP_FRYING = '튀기기',
    STIR_FRYING = '볶기',
    PASTA = '파스타 만들기',
    JAM = '잼 만들기',
    PIE = '파이 만들기',
    STEAMING = '찌기',
    PIZZA = '피자 만들기',
    FERMENTING = '발효',
    SOUS_VIDE = '수비드',
    JULIENNING = '저미기',

    def __str__(self):
        return str(self.value[0])
