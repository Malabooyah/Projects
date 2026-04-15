import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import os

#Sets target website annd creates header so the script is seen like a browser
url="https://file-examples.com/index.php/sample-documents-download/sample-pdf-download/"
headers = {
    "User-Agent": "Mozilla/5.0"
}

#Request the Webpage and prints if it worked or not
response = requests.get(url, headers=headers)
if response.status_code == 200:
    print("Connection Succesful!")
else:
    print("Connection Failed")
    print("Status Code: ", response.status_code)

#Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

#Find all links put them into a list
links= soup.find_all("a")
print("Total links found: ", len(links))

#Extracts and filter document links
pdf_links=[]
for link in links:
    href=link.get("href")
    if isinstance(href, str) and ".pdf" in href.lower():
        full_url=urljoin(url, href)
        pdf_links.append(full_url)

#Print links and how many total links found
print("\nPDF links found: ")
for pdf in pdf_links:
    print(pdf)

print("Total PDFs found: ", len(pdf_links))

#Makes download folder if it does not exist and ignores if it already does
os.makedirs("downloads", exist_ok=True)

#Download Files
for link in pdf_links:
    file_response = requests.get(link, headers=headers)

    if file_response.status_code == (200):
        filename = link.split("/")[-1].split("?")[0]

        with open(f"downloads/{filename}", "wb") as f:
            f.write(file_response.content)

        print(f"Downloaded: {filename}")
    else:
        print(f"Failed to download: {link}")

#Save list of downloaded files to txt

with open("pdf_links.txt", "w") as f:
    for link in pdf_links:
        f.write(link + "\n")
