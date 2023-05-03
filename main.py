import pyshorteners

while True:
    url = input("Enter the URL you want to shorten: ")
    shortener = pyshorteners.Shortener()
    shortened_url = shortener.tinyurl.short(url)
    print("Shortened URL:", shortened_url)