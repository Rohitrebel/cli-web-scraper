# cli-web-scraper

## Times of India Headline Web Scraper

This Python script scrapes the latest headlines from the [Times of India](https://timesofindia.indiatimes.com/) homepage and saves them into a timestamped text file. Ideal for those who want a quick snapshot of daily news without visiting the website.

---

## Features

- Fetches and stores headlines in a `.txt` file named after the current date.
- User-defined limit for the number of headlines to fetch.
- Simple and minimal terminal interface.
- Uses `BeautifulSoup` for web scraping and `requests` for HTTP handling.
- Gracefully handles exceptions and user interruptions (CTRL+C).

---

## How It Works

1. Prompts the user to specify how many headlines to fetch.
2. Scrapes the homepage for `<figcaption>` tags, where headlines are located.
3. Saves the headlines to a local `.txt` file.
4. Delays between fetches using `time.sleep(1)` to avoid overwhelming the server.

---

## Requirements

Install dependencies using:

```bash
pip install -r requirements.txt
```

**requirements.txt**

```
requests
beautifulsoup4
```

---

## How to Run

```bash
python scraper.py
```

---

## Output

A file will be generated in the format:

```
headlines_YYYY-MM-DD.txt
```

![alt text](https://res.cloudinary.com/ddrbrwcvz/image/upload/v1754554444/Screenshot_2686_ir1hkr.png)

## ⚠️ Notes

- If the Times of India changes their HTML structure, you may need to update the tag used (`figcaption`).
- Requires an active internet connection to fetch data.
- Don't overuse scraping—respect website terms of service.

---

## 🙌 Acknowledgements

- [Times of India](https://timesofindia.indiatimes.com/)
- [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
