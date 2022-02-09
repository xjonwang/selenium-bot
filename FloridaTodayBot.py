import pip
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from multiprocessing import Process
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent

chromedriver_location = "C:/Users/xjonw/Github/chromedriver_win32/chromedriver.exe"

close_ad_button = '//*[@id="gnt_mol_oy"]/div/button'
scroll_marker = '/html/body/div[2]/main/article/div[4]/p[14]'
survey_class = 'gnt_em_hf_if'
nish_button = 'PDI_answer50672760'
vote_button = 'pd-vote-button11039223'

'''
options = Options()
ua = UserAgent()
userAgent = ua.random
print(userAgent)
options.add_argument(f'user-agent={userAgent}')
'''



def vote():
    driver = webdriver.Chrome(executable_path = chromedriver_location)
    driver.get('https://www.floridatoday.com/story/sports/high-school/2022/02/07/community-credit-union-florida-athlete-week-ballot/9284769002/')
    for j in range(5):
        try:
            try:
                driver.find_element(By.XPATH, close_ad_button).click()
            except NoSuchElementException:
                print("No Popup Detected")
            
            scroll_marker_element = driver.find_element(By.XPATH, scroll_marker)
            driver.execute_script('arguments[0].scrollIntoView();', scroll_marker_element)
            driver.execute_script('window.scrollBy(0, -100);', '')
            driver.execute_script('window.scrollBy(0, 50);', '')

            driver.switch_to.frame(driver.find_element(By.CLASS_NAME, survey_class))
            driver.find_element(By.ID, nish_button).click()
            driver.find_element(By.ID, vote_button).click()
        except:
            driver.refresh()
            time.sleep(1)
    driver.delete_all_cookies()
    driver.quit()
    print("Here")

def voteInfinite():
    while True:
        vote()

# method to time iterations (currently unused)
def timeme(method):
    def wrapper(*args, **kw):
        startTime = int(round(time.time() * 1000))
        result = method(*args, **kw)
        endTime = int(round(time.time() * 1000))
        print("Execution time: {}".format((endTime - startTime)/1000))
        return result
    return wrapper

if __name__ == '__main__':
    for i in range(10):
        p = Process(target=voteInfinite)
        p.start()


