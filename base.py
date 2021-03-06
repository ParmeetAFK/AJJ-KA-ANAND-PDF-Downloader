import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
from PyPDF2 import PdfFileMerger
from datetime import date
import datetime
import shutil
import os

def connection(url='http://www.google.com/', timeout=5):

	# --------------------------------- Checks Internet Connection -----------------

    try:
        req = requests.get(url, timeout=timeout)
        req.raise_for_status()
        print("You're connected to internet\n")
        return True
    except requests.HTTPError as e:
        print("Checking internet connection failed, status code {0}.".format(
        e.response.status_code))
    except requests.ConnectionError:
        print("No internet connection available.")
    return False

def build_url():

    #------------------------------- Builds URL for todays Newspaper ---------------------------

    u0 = "http://aajkaanand.epapers.in/encyc/625/"

    dt = date.today()

    global date_today

    date_today = str(datetime.date.strftime(dt, "%Y/%m/%d"))

    u1 = date_today + "/Ppage_"

    u2 = u1 + str(page)

    u3 = '.pdf'

    global url

    url = u0 + u2 + u3

    print("Downloading page number --> " + str(page))


def download_pdf():

    # -------------------- Visits webpage and downloads the pdf file ----------------------------------

    r = requests.get(url , allow_redirects=True)
    open(str(page) + '.pdf' ,'wb').write(r.content)


def merge_pdf():

    # ------------------------ Merges all 16 pages of pdf -----------------------------------------

    username = os.getlogin()    # Fetch username
    x = [a for a in os.listdir() if a.endswith(".pdf")]
    merger = PdfFileMerger()

    x.sort(key=lambda item: int(item.split('.')[0]))

    for pdf in x:
        merger.append(open(pdf,'rb'))

    with open(f'C:\\Users\\{username}\\Desktop\\result.pdf','wb') as fout:
        merger.write(fout)


connection()
for page in range(1,17):
    build_url()
    download_pdf()
merge_pdf()
print("Your Newspaper is saved on your Desktop")

