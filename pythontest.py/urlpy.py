import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen as uReq
import os

save_dir='images/'
if not  os.path.exists(save_dir):
    os.makedirs(save_dir)
    query = 'elon musk'
    response = requests.get(f'https://www.google.com/search?q=elon+musk&sca_esv=592464911&hl=en&tbm=isch&sxsrf=AM9HkKk2E7r9cONXbF8Ria15UhFl0B5HXA%3A1703063277987&source=hp&biw=1422&bih=702&ei=7a6CZZDbOYqTseMP8M2CwAk&iflsig=AO6bgOgAAAAAZYK8_XDhCa9Rn9lbslJj8blIQMyHfNPj&oq=elon+&gs_lp=EgNpbWciBWVsb24gKgIIADIIEAAYgAQYsQMyCBAAGIAEGLEDMggQABiABBixAzIIEAAYgAQYsQMyCBAAGIAEGLEDMgUQABiABDIIEAAYgAQYsQMyCBAAGIAEGLEDMggQABiABBixAzIIEAAYgAQYsQNIoDVQmRxYhipwAXgAkAEAmAHRAaABkgeqAQUwLjQuMbgBA8gBAPgBAYoCC2d3cy13aXotaW1nqAIKwgIHECMY6gIYJ8ICBBAjGCfCAgsQABiABBixAxiDAQ&sclient=img)
     reponse                         



    