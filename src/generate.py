import os

from openai import OpenAI

from src.prompt import SYSTEM_PROMPT, get_batch_prompt
from src.types import Card, CardBatch

def generate_batch(words: list[str], mock: bool = False) -> list[Card]:
    if not words:
        return []

    if mock:
        return [Card(english="Mock definition", mandarin="測試", pinyin="cè shì", context="Mock context", example="Mock example")]
        
    try:
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

        response = client.responses.parse(
            model="gpt-4.1-mini-2025-04-14",
            input=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {
                    "role": "user",
                    "content": get_batch_prompt(words),
                },
            ],
            text_format=CardBatch,
        )

        parsed_response: CardBatch = response.output_parsed

        return parsed_response.cards
                
    except Exception as e:
        print(f"Error processing batch {words}: {e}")
        return []
