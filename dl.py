import requests

def download_file(file_url):
    r = requests.get(file_url, stream = True)

    fname = file_url.split("/")[-1]
    with open(fname,"wb") as dl:
        for chunk in r.iter_content(chunk_size=1024):
            # writing one chunk at a time to dl
            if chunk:
                dl.write(chunk)

def get_urls(address="download_these.in"):
    with open(address, "r") as f:
        lines = f.readlines()

    return [x.strip() for x in lines]

if __name__ == '__main__':
    urls = get_urls()
    print(urls)
    for url in urls:
        download_file(url)
