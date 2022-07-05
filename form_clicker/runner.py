from scrapy.utils.log import configure_logging
from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

from form_clicker import settings

from form_clicker.spiders.usdz_spider import UsdzSpider


accounts = [
    {'0x30A2908813698d9a78537E297B640EbAf6990727': 'Htqlm1'},
    {'0x68c4C1E8D3AfB9350da66cee1F36eb115B5Ffce6': 'sssh333',},
    {'0x282860f44c74349C60a2E60e8c9361E4C7bE58F2': 'zhezhbtw',},
    {'0x5E4A4dd838fc3BcD702712FC77fBEe96ff4BBdCB': 'sparkysparkybooman'},
    {'0xFa184D0270dEce069d12b0f3D986b5BA1Ff4bF24': 'wesglufa'},
    {'0xaCE1Ac3c6B29F8ff38574fBa1fBd7a138D8f9E0D': 'shartlov'},
    {'0x9fb81A6e49aC62Ea27c3718dd3C146549425b231': 'kikuc1'},
    {'0x590f129f6bb317aB15878fE7Ea29EDb1d4cB2799': 'az5kdt'},
    {'0xb2Bebb7ecf68A76EB39bce177C41e2880115DA89': 'Pinrol'},
    {'0xbE2950591B859Df73F227060ad7cD4315E859899': 'ai_dont_know'},
    {'0x406674115D6892984137F8458d03fE84dBf70dD4': 'ds11r'},
    {'0xDd0F8f10F9b8cC0fE16dF030Ad6b94dFe02136ab': 'pulpich'},
    {'0xdcd7534a57BCc2C4B742ebA23C0dec687c5A5022': 'Enchantress1337'},
    {'0x251766D9De9B4D6629321c8e5faeD3f03f0E2fB7': 'Sun_1961'},
    {'0x5b299D711b9D4a7447C8DBCbe089E37368dae475': 'Elena_Kassina'},
    {'0x8f2BD081D73a0802D39c1f7Ba736D1B25EEc2566': 'awe_timur'},
    {'0x7c0F8bdBBA958C55e6C55E1b7DBcb6Ca5Fe0d792': 'vital772'},
]

if __name__ == '__main__':
    configure_logging()
    custom_settings = Settings()
    custom_settings.setmodule(settings)

    custom_settings = Settings()
    custom_settings.setmodule(settings)

    process = CrawlerProcess(settings=custom_settings)
    process.crawl(UsdzSpider, accounts=accounts)

    process.start()
