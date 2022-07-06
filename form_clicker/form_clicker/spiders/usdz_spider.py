from scrapy import Spider
from scrapy.http import TextResponse
from scrapy.http import FormRequest

import requests

from form_clicker.items import FormClickerItem

from datetime import datetime


class UsdzSpider(Spider):

    name = 'usdz'
    allowed_domains = ['stablefarm.net']
    start_urls = ['https://stablefarm.net']
    login_url = 'https://api.stablefarm.net/api/account/login/'
    claim_url = 'https://api.stablefarm.net/api/account/user/claim/'

    def __init__(self, accounts):
        super().__init__()
        self.accounts = accounts

    # referral: 2116c559-421f-44aa-9978-568ed8801e42
    def parse(self, response: TextResponse, **kwargs):
        for i in self.accounts:
            wallet = list(i.keys())[0]
            login = i[wallet]
            yield FormRequest(
                self.login_url,
                formdata={
                    'referral': '2116c559-421f-44aa-9978-568ed8801e42',
                    'wallet_address': wallet,
                    'telegram_id': '@' + wallet,
                },
                headers={
                    'Origin': self.start_urls[0],
                    'Referer': self.start_urls[0],
                },
                method='POST',
                callback=self.press_claim_button,
                cb_kwargs={'login': login}
            )

    def press_claim_button(self, response: TextResponse, **kwargs):
        authorization = 'Bearer ' + response.json()['access']
        r = requests.post(self.claim_url, headers={
            'Authorization': authorization,
            'Accept': 'application/json, text/plain, */*',
            'Referrer': self.start_urls[0],
            'sec-ch-ua-platform': 'Windows'
        })
        answer = r.json()
        item = FormClickerItem()
        item['date'] = str(datetime.now())
        item['login'] = kwargs['login']
        item['answer'] = answer

        yield item
