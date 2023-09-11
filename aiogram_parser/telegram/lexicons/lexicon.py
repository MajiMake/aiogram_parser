from dataclasses import dataclass

@dataclass
class LEXICON_RU:
    start: str = '''<b>Привет!</b>\nЯ собираю цены на продукты с разных источников'''
    except_lexicon = ['куплю']
    include_lexicon = ['в наличии', 'заказ', 'заказать', 'продаже', 'гарантия', 'продажа']
