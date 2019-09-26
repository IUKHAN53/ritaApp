from selenium import webdriver
from time import sleep
import os
import zipfile
from selenium.webdriver.chrome.options import Options
from users.forms import FacebookFileAddForm
from datetime import datetime
import random

# datetime object containing current date and time
now = datetime.now()

chrome_options = Options()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--headless")
chrome_options.add_argument('window-size=1200x600')
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")


base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
media_root = os.path.join(base_dir, 'data/user_facebook_data')


def index_html_path(path_to_main):
    process_str = path_to_main.split('/data')[1]
    process_str = '/data'+process_str+'/index.html'
    return process_str


def enable_download(path_to_folder_passed):
    chrome_options.add_experimental_option("prefs", {
      "download.default_directory": path_to_folder_passed,
      "download.prompt_for_download": False,
    })


prefs = {"profile.default_content_setting_values.notifications": 2}

chrome_options.add_experimental_option("prefs", prefs)


def make_dir(user_id):
    hash = random.getrandbits(128)
    dt_string = now.strftime("%d_%m_%Y_%H_%M_%S")
    path_make = f'{media_root}/{user_id}{dt_string}{hash}'
    os.mkdir(path_make)
    return path_make


def unzip(path_passed):
    files = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path_passed):
        for file in f:
            if '.zip' in file:
                files.append(os.path.join(r, file))

    path_to_zip = files[0]
    with zipfile.ZipFile(path_to_zip, 'r') as zip_ref:
        zip_ref.extractall(path_passed)


class fetch:
    def __init__(self, phone_email_passed, password_passed):
        self.driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)
        self.phone_email = phone_email_passed
        self.password = password_passed

    def start(self):
        self.driver.get('https://www.facebook.com/')

    def login(self):
        sleep(5)
        self.driver.implicitly_wait(10)

        phone_email_entry = self.driver.find_element_by_id('email')
        password_entry = self.driver.find_element_by_id('pass')
        phone_email_entry.send_keys(self.phone_email)
        password_entry.send_keys(self.password)

        self.driver.find_element_by_id('loginbutton').click()

        sleep(1)
        self.driver.get('https://www.facebook.com/settings?tab=your_facebook_information')

        if 'You must confirm your password to edit your account settings.' in self.driver.page_source:
            try:
                phone_email_entry = self.driver.find_element_by_id('email')
                password_entry = self.driver.find_element_by_id('pass')
                phone_email_entry.send_keys(self.phone_email)
                password_entry.send_keys(self.password)
                self.driver.find_element_by_id('loginbutton').click()
            except:
                pass
            else:
                sleep(2)

    def click_get_data(self):
        self.driver.get('https://www.facebook.com/settings?tab=your_facebook_information')
        sleep(5)
        self.driver.find_element_by_xpath('//*[@id="SettingsPage_Content"]/ul/li[2]/a/span[1]/span').click()

        self.driver.implicitly_wait(10)

        self.driver.find_element_by_xpath('//div[text()="Create File"]').click()

    def check_data_got(self):
        sleep(1)
        self.driver.get(self.driver.current_url)
        sleep(3)
        try:
            get = self.driver.find_element_by_class_name('_2as-')
        except Exception as e:
            return False
        else:
            return True

    def download_kero(self):
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="content"]/div/div/div/div[2]/div/div/div/ul/li[2]/a/div').click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath('//div[text()="Download"]').click()

        self.driver.implicitly_wait(5)

    def close(self):
        self.driver.close()

    def enale_download(self, path_to_download):
        self.driver.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
        params = {'cmd': 'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': path_to_download}}
        command_result = self.driver.execute("send_command", params)


def run(passed_email, passed_pass, path_to_folder, user):
    main_path = make_dir(user.pk)
    try:
        enable_download(main_path)
        bot = fetch(passed_email, passed_pass)
        bot.enale_download(main_path)
        bot.start()
        bot.login()
        bot.click_get_data()

        while True:
            got_data = bot.check_data_got()
            print('#############################################YESSSSS####################')
            sleep(20)
            if not got_data:
                break

        bot.download_kero()

        sleep(10)
        bot.close()

        unzip(main_path)
    except:
        try:
            os.rmdir(main_path)
        except:
            pass
    else:
        indexhtmlpath = index_html_path(main_path)

        form_hai = FacebookFileAddForm()
        facebookfinal = form_hai.save(commit=False)
        facebookfinal.user = user
        facebookfinal.path_to_facebook_data = indexhtmlpath
        facebookfinal.availible_stat = True
        facebookfinal.save()
