def between_markers(text: str, start: str, end: str) -> str:
    return text[text.find(start) + len(start):text.find(end)]