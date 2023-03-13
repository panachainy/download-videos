import requests
from bs4 import BeautifulSoup
import re
import sys

def get_hls_link_from(url: str):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    textInVidePlayerBg = soup.find(id='video-player-bg')

    html5playerScript = textInVidePlayerBg.find_all('script')[4].text

    match = re.search(r"html5player\.setVideoHLS\('(.+?)'\)",
                      html5playerScript)
    if not match:
        sys.exit()

    return match.group(1)

# sys.modules[__name__] = get_hls_link_from
