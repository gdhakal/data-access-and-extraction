import bs4
from urllib.request import urlopen as uReq # uReq is alias for urlopen
from bs4 import BeautifulSoup as soup # soup is alias for BeautifulSoup

# opens the connection, grabs the webpage, and downloads it
my_url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics+card'
uClient = uReq(my_url) 

# store it in variable so that we can use the data later, otherwise the data will be dumped immediately.
page_html = uClient.read() 

# close the connection
uClient.close() 

# parse the html
page_soup = soup(page_html, "html.parser")

########
# traverse the dom elements of the html page and convert every graphics card you see into a data in a csv file
########

containers = page_soup.findAll("div", {"class": "item-container"})

# open up a new file and write it
filename = "products.csv"
f = open(filename, "w")

# csv file has headers and is delimited by new line
headers = "brand, product_name, shipping\n" 

# first line to be headers
f.write(headers) 

for container in containers:
	brand = container.div.div.a.img["title"]
	title_container = container.findAll("a", {"class" : "item-title"})
	product_name = title_container[0].text
	shipping_container = container.findAll("li", {"class": "price-ship"})
	shipping = shipping_container[0].text.strip() # strip method will remove whitespace (new line, new tab, return) before and after the text 
	f.write(brand + "," + product_name.replace(",", "|") + "," + shipping + "\n") # replace comma in product_name to avoid conflict with deliminator comma

f.close()


