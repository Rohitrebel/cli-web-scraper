import requests, time, os
from bs4 import BeautifulSoup
from datetime import datetime

filename = f"headlines_{datetime.now().strftime('%Y-%m-%d')}.txt"

try:  
  limit = int(input("Specify how many numbe of headlines you want fetch: "))
except ValueError:
  print("Invalid number! Defaulting to 10 headlines")

print("Fetching the headlines...")

url = "https://timesofindia.indiatimes.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

with open(filename, "w") as file:
  file.write("--- Times of India Headlines ---")
  file.write("\n")

count = 0

try:
  print("Processing...") 
  print("Press CTRL+C to stop fetching...")

  for headline in soup.find_all("figcaption"):

    if (count >= limit):
      break

    with open(filename, "a", encoding="utf-8") as file:
      count = count + 1
      file.write(f"{count}. {headline.get_text(strip=True)}")
      file.write("\n")

    time.sleep(1)

  if count:
    print("Number of headlines fetched:", count)      
    print("Fetching Completed")
  else:
    print("Couldn't find the requested data, Check tags")   

except KeyboardInterrupt:
  print("Fetching Stopped...") 

except Exception as err:
  print("Error Occured: ",  err)

