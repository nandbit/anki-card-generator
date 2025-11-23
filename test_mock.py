import csv
from src.generate import fetch_card_data

OUTPUT_FILE: str = "test_anki_import.txt"

def test_generation() -> None:
    mock_words: list[str] = ["apple", "run", "happy"]
    
    print("Running mock generation...")
    
    with open(OUTPUT_FILE, "w", encoding="utf-8", newline='') as f:
        writer = csv.writer(f, delimiter=';', quoting=csv.QUOTE_MINIMAL)
        
        for word in mock_words:
            data: dict[str, str] | None = fetch_card_data(word, mock=True)
            
            if data:
                row: list[str] = [
                    data.get("english", ""),
                    data.get("mandarin", ""),
                    data.get("pinyin", ""),
                    data.get("context", ""),
                    data.get("example", "")
                ]
                writer.writerow(row)
                print(f"Generated mock card for: {word}")

    print(f"Test complete. Check {OUTPUT_FILE}")

if __name__ == "__main__":
    test_generation()
