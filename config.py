headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0"
}

start_link = "https://www.kijiji.ca/b-apartments-condos/city-of-toronto/c37l1700273"

start_page = 1
finish_page = 2


def get_url(page_number=1):
    return f"https://www.kijiji.ca/b-apartments-condos/city-of-toronto/page-{page_number}/c37l1700273"
