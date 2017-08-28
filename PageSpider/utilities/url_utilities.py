from urllib.request import urlopen


def load_url_from_files(file_path: str):
    try:
        with open(file_path) as f:
            content = f.readline()
            return content
    except FileNotFoundError:
        print("The file " + file_path+" could not be found")
        exit(2)


def load_page(url: str):
    response = urlopen(url)
    html=response.read().decode('utf-8')
    return


def scrape_page(page_content: str):
    # TODO: analyze the text
    pass
