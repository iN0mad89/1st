from dataclasses import dataclass
from typing import List

@dataclass
class Category:
    name: str
    priority: int

# Priority order as defined by the project requirements
CATEGORY_PRIORITY = [
    'Нечинний',
    'Бюджет',
    'Науковець',
    'Інститут',
    'базис ННТД',
    'Регулювання',
    'Статус',
    'Омонім',
]

CATEGORIES: List[Category] = [
    Category(name=name, priority=idx) for idx, name in enumerate(CATEGORY_PRIORITY)
]

CATEGORY_INDEX = {cat.name: cat for cat in CATEGORIES}
