"""
© 2022 By Bert.
Async-based API Scrapper module.

Based on ImJustGood API
Official docs: https://api.imjustgood.com/apidoc.html

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The MIT License (MIT)

Copyright © 2022 by Bert.

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

from urllib.parse import urlparse, parse_qs, quote_plus
import aiohttp

class imjustgood:
    HOST_URL = 'https://api.imjustgood.com'
    
    def __init__(self, apikey: str):
        self._key = apikey
        self._headers = {
            'apikey': apikey,
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36'
        }

    async def _make_request(self, method: str, path: str, return_as_json=True, **kwargs):
        async with aiohttp.ClientSession(headers=self._headers) as session:
            async with session.request(method, self.HOST_URL + path, **kwargs) as request:
                if request.status != 200:
                    raise Exception('Invalid Return Code from server! (Response code -> {})'.format(request.status))
                if return_as_json:
                    data = await request.json()
                    if data['status'] != 200:
                        raise Exception(data['message'])
                    return data
                return bytes(await request.read()).decode('utf-8')

    def apikeyStatus(self, apikey=None):
        params = {'apikey': self._key}
        if apikey:
            self._headers['apikey'] = apikey
            params['apikey'] = apikey      
        return self._make_request('GET', '/status', params=params)

    def youtubeSearch(self, query: str):
        return self._make_request('GET', '/youtube={}'.format(query))

    def youtubeDl(self, url: str):
        if not url.startswith('https://youtu.be'):
            url = 'https://youtu.be/{}'.format(parse_qs(urlparse(url).query)['v'][0])
        return self._make_request('GET', '/youtubedl={}'.format(url))

    def jooxAudio(self, query: str):
        return self._make_request('GET', '/joox={}'.format(query))

    def findLyrics(self, query: str):
        return self._make_request('GET', '/lyric={}'.format(query))

    def findChords(self, query: str):
        return self._make_request('GET', '/chord={}'.format(query))

    def smuleUser(self, username: str):
        return self._make_request('GET', '/smule={}'.format(username))

    def smuleDl(self, post_url: str):
        return self._make_request('GET', '/smuledl={}'.format(post_url))

    def tiktokUser(self, username: str):
        return self._make_request('GET', '/tiktok={}'.format(username))

    def tiktokDl(self, post_url: str):
        return self._make_request('GET', '/tiktokdl={}'.format(post_url))

    def instagramUser(self, username: str):
        return self._make_request('GET', '/instagram={}'.format(username))

    def instagramPost(self, post_url: str):
        return self._make_request('GET', '/instapost={}'.format(post_url))

    def instagramStory(self, username: str):
        return self._make_request('GET', '/instastory={}'.format(username))

    def twitterProfile(self, username: str):
        return self._make_request('GET', '/twitter={}'.format(username))

    def twitterDl(self, post_url: str):
        params = {'url': post_url}
        return self._make_request('GET', '/twitter/video', params=params)

    def facebookDl(self, post_url: str):
        params = {'url': post_url}
        return self._make_request('GET', '/facebook/video', params=params)

    def pinterestDl(self, post_url: str):
        params = {'url': post_url}
        return self._make_request('GET', '/pinterest', params=params)

    def githubProfile(self, username: str):
        return self._make_request('GET', '/github={}'.format(username))

    def lineSQRLogin(self, app_name: str, sys_name: str, cert: str=None):
        self._headers['appName'] = app_name
        self._headers['sysName'] = sys_name
        if cert:
            self._headers['cert'] = cert
        return self._make_request('GET', '/lineqr')

    def lineSQRPin(self, callback_pin_url: str):
        return self._make_request('GET', callback_pin_url)

    def lineSQRAuthToken(self, callback_auth_token_url: str):
        return self._make_request('GET', callback_auth_token_url)

    def lineVOOM(self, post_url: str):
        return self._make_request('GET', '/timeline={}'.format(post_url))

    def googleSearch(self, query: str):
        return self._make_request('GET', '/search={}'.format(query))

    def googleImage(self, query: str):
        return self._make_request('GET', '/image={}'.format(query))

    def googlePlaystore(self, app_name: str):
        return self._make_request('GET', '/playstore={}'.format(app_name))

    def googleTranslate(self, language: str, query: str):
        return self._make_request('GET', '/translate/{}={}'.format(language, query))

    def wallpaperHD(self, query: str):
        return self._make_request('GET', '/wallpaper={}'.format(query))

    def pornVideos(self, query: str):
        return self._make_request('GET', '/porn={}'.format(query))

    def pornStar(self):
        return self._make_request('GET', '/pornstar')

    def hentai(self):
        return self._make_request('GET', '/hentai')

    def kamasutra(self):
        return self._make_request('GET', '/kamasutra')

    def dickAnalyze(self):
        return self._make_request('GET', '/dick')

    def titsAnalyze(self):
        return self._make_request('GET', '/tits')

    def vaginaAnalyze(self):
        return self._make_request('GET', '/vagina')

    def memeGenerator(self, text_1: str, text_2: str, image_url: str):
        return self._make_request('GET', '/meme/{}/{}/url={}'.format(text_1, text_2, image_url))

    def movieReview(self, movie_name: str):
        return self._make_request('GET', '/movie={}'.format(movie_name))

    def movieQuotes(self):
        return self._make_request('GET', '/movie/quotes')

    def cinema21(self, city_name: str):
        return self._make_request('GET', '/cinema={}'.format(city_name))

    def tinyUrl(self, source_url: str):
        return self._make_request('GET', '/tinyurl={}'.format(source_url))

    def bitly(self, source_url: str):
        return self._make_request('GET', '/bitly={}'.format(source_url))

    def kbbiIndonesia(self, query: str):
        return self._make_request('GET', '/kbbi={}'.format(query))

    def smuleUser(self):
        return self._make_request('GET', '/topnews')

    def wikipedia(self, query: str):
        return self._make_request('GET', '/wikipedia={}'.format(query))

    def urbandict(self, query: str):
        return self._make_request('GET', '/urban={}'.format(query))

    def dailyZodiac(self, zodiac_name: str):
        return self._make_request('GET', '/zodiac={}'.format(zodiac_name))

    def alQuran(self, query: str):
        return self._make_request('GET', '/alquran={}'.format(query))

    def bible(self):
        return self._make_request('GET', '/bible')

    def adzan(self, city_name: str):
        return self._make_request('GET', '/adzan={}'.format(city_name))

    def weather(self, city_name: str):
        return self._make_request('GET', '/cuaca={}'.format(city_name))

    def bmkgEarthquake(self):
        return self._make_request('GET', '/bmkg')

    def corona(self):
        return self._make_request('GET', '/corona')

    def lowonganKerja(self):
        return self._make_request('GET', '/karir')

    def cekResi(self, courier: str, bill_number: str):
        return self._make_request('GET', '/resi/{}={}'.format(courier, bill_number))

    def phoneInfo(self, query: str):
        return self._make_request('GET', '/cell={}'.format(query))

    def birthInfo(self, date_time: str):
        return self._make_request('GET', '/lahir={}'.format(date_time))

    def dateInfo(self, date_time: str):
        return self._make_request('GET', '/jadian={}'.format(date_time))

    def artiNama(self, name: str):
        return self._make_request('GET', '/nama={}'.format(name))

    def artiMimpi(self, query: str):
        return self._make_request('GET', '/mimpi={}'.format(query))

    def acaraTVSekarang(self):
        return self._make_request('GET', '/acaratv/now')

    def acaraTVStasiun(self, channel_name: str):
        return self._make_request('GET', '/acaratv={}'.format(channel_name))

    def cctvCode(self):
        return self._make_request('GET', '/cctv/code')

    def cctvSearch(self, cctv_code: str):
        return self._make_request('GET', '/cctv/search/id={}'.format(cctv_code))

    def searchManga(self, title: str):
        return self._make_request('GET', '/manga/search={}'.format(title))

    def chapterManga(self, chapter: str):
        return self._make_request('GET', '/manga/chapter={}'.format(chapter))

    def screenshotWeb(self, source_url: str):
        params = {'url': source_url}
        return self._make_request('GET', '/screenshot', params=params)

    def searchGif(self, query: str):
        return self._make_request('GET', '/gif={}'.format(query))

    def imageToURL(self, file_path):
        return self._make_request("POST", '/imgurl', files={'file': open(file_path, 'rb')})

    def textToImage(self, text: str):
        params = {'text': text}
        return self._make_request('GET', '/imgtext', params=params)

    def watermarkText(self, image_url: str, text: str):
        params = {'image': image_url, 'text': text}
        return self._make_request('GET', '/watermark/text', params=params)

    def watermarkImage(self, image_url: str, icon_url: str):
        params={'image': image_url, 'icon': icon_url}
        return self._make_request('GET', '/watermark/image', params=params)

    def simisimiChat(self, text: str):
        params = {'text': text}
        return self._make_request('GET', '/simisimi')

    def imageStampList(self):
        return self._make_request('GET', '/stamplist')

    def imageStamp(self, image_url: str, number: str):
        params = {'url': image_url, 'num': number}
        return self._make_request('GET', '/stamp', params=params)

    def fanSign(self, text: str, number: str):
        params = {'text': text, 'num': number}
        return self._make_request('GET', '/fansign', params=params)

    def calculator(self, query: str):
        return self._make_request('GET', '/calc={}'.format(query))

    def languageCodes(self):
        return self._make_request('GET', '/language/code')

    def checkIpAddress(self, ip_address: str):
        return self._make_request('GET', '/ip={}'.format(ip_address))

    def binaryEncode(self, text: str):
        params = {'q': text}
        return self._make_request('GET', '/binary/text', params=params)

    def binaryDecode(self, binary_string: str):
        params = {'q': binary_string}
        return self._make_request('GET', '/binary/digit', params=params)

    def base64Encode(self, text: str):
        params = {'q': text}
        return self._make_request('GET', '/base64/text', params=params)

    def base64Decode(self, base_64_string: str):
        params = {'q': base_64_string}
        return self._make_request('GET', '/base64/code', params=params)

    def asciiText(self, text: str):
        return self._make_request('GET', '/ascii={}'.format(text), False)

    def fancyText(self, text: str):
        params = {'text': text}
        return self._make_request('GET', '/fancy', params=params)

    def customURL(self, source_url: str, label: str):
        self._headers['url'] = source_url
        self._headers['label'] = quote_plus(label)
        return self._make_request('GET', '/custom/make')

    def lineAppVersion(self):
        return self._make_request('GET', '/line')