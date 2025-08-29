morse_code_dict: dict[str, str] = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    ' ': '/','.': '.-.-.-',',': '--..--','?': '..--..',"'" : '.----.','!': '-.-.--', 
    '/':'-..-.', '(': '-.--.', ')': '-.--.-', ':' : '---...', ';' : '-.-.-.', '=' : '-...-',
    '-': '-....-', '_' : '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.',
    '+': '.-.-.',
}
reverse_morse_code_dict = {v: k for k, v in morse_code_dict.items()}

def convert_to_morse_code(text: str) -> str:
    return ' '.join(morse_code_dict.get(char.upper(), '?') for char in text)

def convert_to_text(text: str) -> str:
    text  = text.split(' ')
    return ' '.join(reverse_morse_code_dict.get(morse,'?') for morse in text)

def main() -> None:
    text = input("Enter text to convert to Morse code: ")
    morse_code = convert_to_morse_code(text)
    print("\nMorse Code:")
    print(morse_code)
    text1 = convert_to_text(morse_code)
    print("\nText:")
    print(text1)

if __name__ == "__main__":
    main()
