## Task: Create an Emoji cypher

# Dictionary mapping letters and special characters to emojis
emoji = {
    'A': '😀', 'B': '😁', 'C': '😂', 'D': '🤣', 'E': '😃',
    'F': '😄', 'G': '😅', 'H': '😆', 'I': '😉', 'J': '😊',
    'K': '😋', 'L': '😎', 'M': '😍', 'N': '😘', 'O': '🥰',
    'P': '😗', 'Q': '😙', 'R': '😚', 'S': '☺️', 'T': '🙂',
    'U': '🤗', 'V': '🤩', 'W': '🤔', 'X': '🤨', 'Y': '😐',
    'Z': '😑', 'Æ': '🥶', 'Ø': '🤠', 'Å': '🤑'
}

def emoji_cypher(input_text):
    """
    Convert a given text into an emoji cypher.

    Parameters:
    input_text (str): The input text to be converted

    Returns:
    str: The converted text with emojis
    """
    # Convert input text to uppercase
    input_text = input_text.upper()

    # Initialize an empty list to store the output
    output_list = []

    # Iterate through each character in the input text
    for char in input_text:
        if char in emoji:
            # Append the corresponding emoji to output_list
            output_list.append(emoji[char])
        else:
            # If the character is not in the emoji dictionary, append the character itself
            output_list.append(char)

    # Join the list into a single string and return it
    return "".join(output_list)

# Get input from the user
user_input = input("Your Input: ")

# Convert the input to an emoji cypher and print the result
print(emoji_cypher(user_input))
