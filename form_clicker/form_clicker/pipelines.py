import json


class FormClickerPipeline:
    def process_item(self, item, spider):
        doc = {item["date"]: f'{item["login"]}: {item["answer"]}'}
        print(doc)
        return item
