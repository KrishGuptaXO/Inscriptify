def clean_text(text):
    text = text.replace('\n\n', '\n')
    text = text.replace('  ', ' ')
    return text.strip()
