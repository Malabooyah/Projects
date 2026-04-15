# Document Link Parser

A Python project that parses a webpage, extracts PDF links, and downloads them locally.

## Features

- Connects to a webpage using requests
- Parses HTML using BeautifulSoup
- Extracts all links from the page
- Filters for PDF documents
- Downloads PDF files into a local folder
- Saves all found links to a text file

## Technologies Used

- Python
- requests
- BeautifulSoup
- urllib
- os

## How It Works

1. Sends a request to a target webpage
2. Parses the HTML content
3. Extracts all anchor tags
4. Filters links containing ".pdf"
5. Downloads each file to a local folder

## Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

python parser.py
