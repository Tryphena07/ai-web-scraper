MAX_CHARS = 12000

def validate_content(text: str) -> str:
    if not text:
        raise ValueError("Extracted content is empty")

    if len(text) < 200:
        raise ValueError("Content too short to summarize")

    if len(text) > MAX_CHARS:
        print(f"⚠️ Content too large ({len(text)} chars). Truncating to {MAX_CHARS}.")
        return text[:MAX_CHARS]

    return text
