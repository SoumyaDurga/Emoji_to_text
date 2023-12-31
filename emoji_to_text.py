import emoji

def emoji_to_text(input_text):
    # Replace emojis in the input text with their textual representations
    text_with_emojis_converted = emoji.demojize(input_text)
    return text_with_emojis_converted

input_text = "I love 🍕 and 🍦!"
converted_text = emoji_to_text(input_text)
print(converted_text)