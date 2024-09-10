
import scrapy
from hh_scrape.items import HhScrapeItem

class HhSpider(scrapy.Spider):
    name = "hh"
    start_urls = [
        'https://hh.ru/search/vacancy?text=%D0%B4%D0%B0%D1%82%D0%B0-%D0%B8%D0%BD%D0%B6%D0%B5%D0%BD%D0%B5%D1%80&salary=&ored_clusters=true&hhtmFrom=vacancy_search_list&hhtmFromLabel=vacancy_search_line&page=0'
    ]

    def parse(self, response):
        base_url = response.url.split('&page=')[0]
        QUANTITY_PAGES = 6
        
        for i in range(QUANTITY_PAGES):
            url = f'{base_url}&page={i}'
            self.logger.info(f'URL страницы: {url}')
            yield scrapy.Request(url=url, callback=self.parse_page)

    def parse_page(self, response):
        self.logger.info(f'Обрабатываем страницу: {response.url}')
        # Найти все элементы вакансий на странице
        vacancies = response.xpath('//div[contains(@class, "magritte-redesign")]')

        for vacancy in vacancies:
            title = vacancy.xpath('.//span[@data-qa="serp-item__title-text"]/text()').get()
            href = vacancy.xpath('.//a[@data-qa="serp-item__title"]/@href').get()
            solary = vacancy.xpath(".//span[@class='magritte-text___pbpft_3-0-14 magritte-text_style-primary___AQ7MW_3-0-14 magritte-text_typography-label-1-regular___pi3R-_3-0-14']//text()").getall()
            
            # Логируем и сохраняем данные
            self.logger.info(f'Заголовок вакансии: {title}')     
            self.logger.info(f'Ссылка вакансии: {href}')     
            self.logger.info(f'Зарплата: {solary}')     

            yield HhScrapeItem(title=title,href=href,solary=solary)

       