hebrew_letters = {
    "א": 1, "ב": 2, "ג": 3, "ד": 4, "ה": 5, "ו": 6, "ז": 7,
    "ח": 8, "ט": 9, "י": 10, "כ": 20, "ל": 30, "מ": 40,
    "נ": 50, "ס": 60, "ע": 70, "פ": 80, "צ": 90, "ק": 100,
    "ר": 200, "ש": 300, "ת": 400
}

def calculate_hebrew_gematria(word):
    """Calculate the Gematria value of a Hebrew word."""
    return sum(hebrew_letters.get(char, 0) for char in word)

def calculate_english_gematria(text: str) -> int:
    """Calculate the English Gematria of a given text."""
    english_mapping = {chr(i): i - 64 for i in range(65, 91)}  # A=1, B=2, ..., Z=26
    total = 0
    for char in text.upper():
        total += english_mapping.get(char, 0)
    return total

def atbash_cipher(word):
    """Apply Atbash cipher (reverse Gematria) to a word."""
    reversed_letters = {k: v for k, v in zip(hebrew_letters.keys(), reversed(hebrew_letters.values()))}
    return sum(reversed_letters.get(char, 0) for char in word)

# Example usage
if __name__ == "__main__":
    print(calculate_gematria("בראשית"))  # Example: Genesis
    print(atbash_cipher("בראשית"))      # Example: Atbash
