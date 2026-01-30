import trafilatura

def clean_html(html: str) -> str:
    """
    Extract main readable text from HTML using Trafilatura.
    """
    text = trafilatura.extract(
        html,
        include_comments=False,
        include_tables=False,
        no_fallback=True
    )

    if not text:
        raise ValueError("Trafilatura could not extract main content")

    return text
