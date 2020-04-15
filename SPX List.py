import bs4 as bs
import requests
import pandas as pd
 
def save_sp500_tickers():
    resp = requests.get('http://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    soup = bs.BeautifulSoup(resp.text, 'lxml')
    table = soup.find('table', {'class': 'wikitable sortable'})

    tickers = []
    industries = []

    for row in table.findAll('tr')[1:]:
            ticker = row.findAll('td')[0].text
            industry = row.findAll('td')[4].text

            tickers.append(ticker)
            industries.append(industry)

    tickers = list(map(lambda s: s.strip(), tickers))
    industries = list(map(lambda s: s.strip(), industries))

    tickerdf = pd.DataFrame(tickers,columns=['ticker'])
    sectordf = pd.DataFrame(industries,columns=['industry'])

    tickerandsector = pd.concat([tickerdf, sectordf], axis=1, join_axes=[tickerdf.index])
   
    tickerandsector.to_csv(r'E.....\Python Projects\SPX List\SPXTickerIndustry.csv', index = False) 
    return tickerandsector

save_sp500_tickers()
