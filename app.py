from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import playlist as p
import rpi

#Func
def read_title(artist='Bruno Mars',name='Treasure'):
    search = artist + '+' + name + '+' + 'lyric'
    driver.get(f"https://www.youtube.com/results?search_query={search}")
    driver.implicitly_wait(2)
    selection = driver.find_element_by_id("video-title")
    selection.click()

    driver.implicitly_wait(2)
    temp = driver.find_element_by_class_name("ytp-time-duration").get_attribute("innerHTML").split(sep=":")
    temp = [int(i) for i in temp]

    if len(temp) >= 3 :
        t = 5*60
    elif len(temp) ==2 :
        t = temp[0]*60+temp[1]-2
    elif len(temp) == 1 :
        t = temp[0]
    else :
        print("Timestamp not found, waiting 10 sec")
        t = 10
    time.sleep(t)
    driver.get("https://www.youtube.com")

def play(gtr:p.getter):
    temp = gtr.get_track()
    read_title(artist=temp[1],name=temp[0])

#Init
options = Options()
options.binary_location = "C:\Program Files\BraveSoftware\Brave-Browser\Application\\brave.exe"
driver_path = 'C:\chromedriver'
driver = webdriver.Chrome(options = options, executable_path = driver_path)
driver.get('https://www.youtube.com/')


def access_youtube() : 
    driver.implicitly_wait(2)
    bouton = driver.find_element_by_xpath("//button[@aria-label=\"Accepter l\'utilisation de cookies et autres données aux fins décrites ci-dessus\"]")
    bouton.click()
    driver.implicitly_wait(2)

#v Write code below v
access_youtube()

my_getter = p.getter()


while True :
    
    if rpi.light :
        access_youtube()
        play(my_getter)





