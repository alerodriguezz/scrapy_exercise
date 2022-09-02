import scrapy

class CourtScraper(scrapy.Spider):
  name = 'events'
  start_urls = ["https://coinmarketcal.com/en/"]



  def parse(self,response):
    print(response)
    
    rows = response.xpath("/html/body/main/section[1]/div[2]/div[3]/article")
    for i in range(1,len(rows)):
      yield{
        'event_date': rows[i].xpath('div/div/a/h5[1]/text()').get(),
        'event_name': rows[i].xpath('div/div/a/h5[2]/text()').get(),
        'event_description': rows[i].xpath('div/div/div/p/text()').get().strip().replace('"',"")
      }

    next_page = response.xpath('//a[contains(text(), ">")]')
    if next_page is not None:
      yield response.follow( response.xpath('//a[contains(text(), ">")]').attrib['href'], callback=self.parse)
      