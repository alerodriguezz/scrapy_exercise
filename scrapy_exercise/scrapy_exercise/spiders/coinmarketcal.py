import scrapy

class CourtScraper(scrapy.Spider):
  name = 'events'
  start_urls = ["https://coinmarketcal.com/en/"]



  def parse(self,response):
    print(response)
    """
    rows = response.xpath('/html/body/font[1]/table[2]/tr')
    for i in range(1,len(rows)):
      yield{
        'id': rows[i].xpath('td[1]/text()').extract()[0] ,
        'name':rows[i].xpath('td[2]/text()').extract()[0],
        'address':rows[i].xpath('td[3]/text()').extract()[0],
        'party type':rows[i].xpath('td[4]/text()').extract()[0],
        'party end date':rows[i].xpath('td[5]/text()').extract()[0],
        'filing date':rows[i].xpath('td[6]/text()').extract()[0],
        'case status':rows[i].xpath('td[7]/text()').extract()[0]
      }
    next_page = response.xpath('//a[contains(text(), "Next")]')
    if next_page is not None:
      yield response.follow( response.xpath('//a[contains(text(), "Next")]').attrib['href'], callback=self.parse)
      """