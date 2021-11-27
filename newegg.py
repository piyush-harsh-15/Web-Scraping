from bs4 import BeautifulSoup
import requests

# HTML From Website
url = "https://www.newegg.ca/gigabyte-geforce-rtx-3080-gv-n3080vision-oc-10gd/p/N82E16814932460"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

prices = doc.find_all(text="$")
parent = prices[0].parent
strong = parent.find("strong")
print(strong.string)