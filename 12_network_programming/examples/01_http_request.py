"""\nHTTP Request\n\n"""\n\nfrom urllib.request import urlopen

url = "https://example.com"
with urlopen(url) as response:
    print(response.status)
    print(response.read(200).decode("utf-8", errors="replace"))\n