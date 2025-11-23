from pydantic import BaseModel

class Card(BaseModel):
    english: str
    mandarin: str
    pinyin: str
    context: str
    example: str


class CardBatch(BaseModel):
    cards: list[Card]


