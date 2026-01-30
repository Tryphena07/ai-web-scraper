from scraper import fetch_webpage
from cleaner import clean_html
from validator import validate_content
from summarizer import summarize

def run(url: str):
    print("Fetching webpage...")
    html = fetch_webpage(url)

    print("Cleaning content...")
    clean_text = clean_html(html)

    print("Validating content...")
    clean_text = validate_content(clean_text)

    print("Summarizing...")
    summary = summarize(clean_text)

    print("\n--- SUMMARY ---\n")
    print(summary)

if __name__ == "__main__":
    while True:
        url = input("Enter a URL: ").strip()

        if not url:
            print("❌ URL cannot be empty.\n")
            continue

        if not url.startswith("http"):
            print("❌ URL must start with http:// or https://\n")
            continue

        break

    run(url)
