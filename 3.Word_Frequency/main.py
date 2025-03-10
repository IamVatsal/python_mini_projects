from collections import Counter
import re
from tkinter import filedialog

def word_frequency(text: str) -> list[tuple[str, int]]:
    lowered_text = text.lower()
    words = re.findall(r'\b\w+\b', lowered_text)
    word_counter = Counter(words)
    word_frequency = word_counter.most_common(n=10)
    return word_frequency


def main():
    print("Welcome to the Word Frequency Counter I am going to count the frequency of words in a text file")
    print("Showing the top 10 most frequent words")
    
    while True:
        file_location: str = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        try:
            with open(file_location, "r") as file:
                content = file.read()
            word_count = word_frequency(content)
            for word, frequency in word_count:
                print(f"{word}: {frequency}")
            break
        except FileNotFoundError:
            print("File not found. Please enter a valid path to the file.")
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()