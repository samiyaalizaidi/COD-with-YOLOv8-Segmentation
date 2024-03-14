import hashlib, io, requests, pandas as pd
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from bs4 import BeautifulSoup
from pathlib import Path
from PIL import Image

options = ChromeOptions()
options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)

driver.get("https://www.google.com/search?sca_esv=da56b67854fd2398&rlz=1C1CHBF_enPK1018PK1018&sxsrf=ACQVn0_Ig9_mGrSIlWYry-bwtrj-NZhF2Q:1710398074090&q=grasshopper+actual+images&tbm=isch&source=lnms&sa=X&ved=2ahUKEwjKsYWtkfOEAxXL_rsIHQFzDUsQ0pQJegQICxAB&biw=1280&bih=593&dpr=1.5")
content = driver.page_source
soup = BeautifulSoup(content, "html.parser")
driver.quit()

def gets_url(classes, location, source):
    results = []
    for a in soup.findAll(attrs={"class": classes}):
        name = a.find(location)
        if name not in results:
            results.append(name.get(source))
    return results

if __name__ == "__main__":
    returned_results = gets_url("s-item__image-wrapper image-treatment", "img", "src")
    for b in returned_results:
        image_content = requests.get(b).content
        image_file = io.BytesIO(image_content)
        image = Image.open(image_file).convert("RGB")
        file_path = Path(r'C:\Users\computer house\OneDrive - Habib University\Semesters\Semester 6\Computer Vision\SCRAPPPP', hashlib.sha1(image_content).hexdigest()[:10] + ".png")
        image.save(file_path, "PNG", quality=80)
