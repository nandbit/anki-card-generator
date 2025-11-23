import csv
import os
from dotenv import load_dotenv

from src.types import Card
from src.utils import chunk_list
from src.generate import generate_batch
from src.config import INPUT_FILE, OUTPUT_FILE, BATCH_SIZE

load_dotenv()

def create_output_file(output_file: str) -> None:
    if (len(output_file) == 0):
        raise ValueError("Error: output file path is empty")

    # Remove the trailing slash for the next call of os.path.split
    if (output_file[-1] == '/'):
        output_file = output_file[:-1]

    head, tail = os.path.split(output_file)

    os.makedirs(head, exist_ok=True)

def extract_words_from_file(file: str) -> list[str] | None:
    if not os.path.exists(file):
        print(f"No file {file} found")
        return

    with open(file, "r", encoding="utf-8") as f:
        words: list[str] = [line.strip() for line in f if line.strip()]

        if not words:
            print(f"No words found in file {file}")
            return

        return words


def output_cards_to_file(output_file: str, words: list[str], batch_size: int):
    create_output_file(output_file)

    with open(output_file, "w", encoding="utf-8", newline='') as f:
        writer = csv.writer(f, delimiter=';', quoting=csv.QUOTE_MINIMAL)
        
        for batch in chunk_list(words, batch_size):
            print(f"Processing batch: {batch}")
            
            cards: list[Card] = generate_batch(batch)
            
            for card in cards:
                row: list[str] = [
                    card.english,
                    card.mandarin,
                    card.pinyin,
                    card.context,
                    card.example
                ]
                writer.writerow(row)

def main() -> None:
    words = extract_words_from_file(INPUT_FILE)
    
    if (not words) or (len(words) == 0):
        return

    output_cards_to_file(OUTPUT_FILE, words, BATCH_SIZE)
    
    
    print(f"Done. Output saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
