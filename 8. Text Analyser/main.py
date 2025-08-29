from collections import Counter

def open_file(file_path: str) -> str:
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print("File not found")
        return ""
    except Exception as e:
        print("Error:", e)
        return ""

def analyze_text(text: str) -> dict:
    words = text.split()
    unique_words = set(words)
    paragraphs = [p for p in text.split('\n\n') if p.strip()]
    word_counts = Counter(words)
    top_5_words = word_counts.most_common(5)

    result: dict = {
        'Top_5_Most_Frequent_Words': top_5_words,
        'Length_including_spaces': len(text),
        'Length_excluding_spaces': len(text.replace(" ", "")),
        'Length_excluding_newlines': len(text.replace("\n", "")),
        'Length_excluding_both': len(text.replace(" ", "").replace("\n", "")),
        'Average_Word_Length': sum(len(word) for word in words) / len(words) if words else 0,
        'Total_Spaces': text.count(" "),
        'Total_Newlines': text.count("\n"),
        'Total_Paragraphs': len(paragraphs),
        'Total_Words': len(words),
        'Total_Unique_Words': len(unique_words),
        'Lines': len(text.splitlines()),
        'Paragraphs': len(paragraphs)
    }
    return result

def main() -> None:
    text = open_file('sample.txt')
    print("\nThis Text File Contains:")
    print(text[:10], '...', text[-10:]) # This Prints the first 10 and last 10 characters
    print("\nText Analysis:")
    if text:
        analysis = analyze_text(text)
        for key, value in analysis.items():
            print(f"{key}: {value}")

if __name__ == "__main__":
    main()
