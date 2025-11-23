## Introduction
An Anki card generator powered by the OpenAI API.

## Input & Output
### Input
A plain file the name of which is specified in `src/config.py`. The file must contain a list of words either in English or Mandarin separated by newlines.

### Output
A txt file the name/directory of which is specified in `src/config.py`.

### Example
Input file: `words.txt`
```
Apple
```

Output file: `output/cards.txt`
```
Apple;蘋果;píng guǒ;Common fruit;我喜歡吃蘋果。<br>wǒ xǐhuān chī píngguǒ<br>I like eating apples.
```

## API Key
place the OpenAI API key in a `.env` file. You can just raname the `.env.example` file.

## Card format
Each card object must have these fields:
1. English: English definition.
2. Mandarin Character(s): Traditional Chinese character(s).
3. Pinyin: Pinyin with tone marks.
4. Context: Brief nuance/context.
5. Example Sentence: Sentence in Traditional Chinese + Pinyin + English translation (separated by <br>).
