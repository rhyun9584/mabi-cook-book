from enum import Enum, auto


class Method(Enum):
    """
    cook 모델에 들어갈 cooking method enum
    """
    MIXING = auto(),
    BAKING = auto(),
    SIMMERING = auto(),     # 삶기
    KNEADING = auto(),      # 반죽
    BOILING = auto(),
    NOODLE = auto(),
    DEEP_FRYING = auto(),   # 튀기기
    STIR_FRYING = auto(),   # 볶기
    PASTA = auto(),
    JAM = auto(),
    PIE = auto(),
    STEAMING = auto(),
    PIZZA = auto(),
    FERMENTING = auto(),    # 저미기
    SOUS_VIDE = auto(),     # 수비드
    JULIENNING = auto(),
