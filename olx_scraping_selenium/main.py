import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.olx.pl/elektronika/telefony/q-iphone/?search%5Border%5D=created_at:desc&search%5Bfilter_enum_state%5D%5B0%5D=used&search%5Bfilter_enum_phonemodel%5D%5B0%5D=iphone-x')
results = []
other_results = []
links=[]
content = driver.page_source
soup = BeautifulSoup(content, 'html.parser')

for a in soup.find_all(attrs={'class': 'css-1venxj6'}):
    name = a.find('h6')
    if name not in results:
        results.append(name.text)

for b in soup.find_all(attrs={'class': 'css-1venxj6'}):
    name2 = b.find(attrs={'class': 'css-13afqrm'})
    if name2 not in other_results:
        other_results.append(getattr(name2, 'text'))

links = [element['href'] for element in soup.find_all(attrs={'class': 'css-z3gu2d'})]

series1 = pd.Series(results, name='Names')
print(series1)
series2 = pd.Series(other_results, name='Prices')
print(series2)
series3 = pd.Series(links, name='Links')
print(series3)
df = pd.DataFrame({'Names': series1, 'Prices': series2, 'Links': series3})
df.to_csv('products.csv', index=False, encoding='utf-8')