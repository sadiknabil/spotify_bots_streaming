from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from threading import Lock
from random import choice,randint
from colorama import init,Fore,Style
from time import sleep
from os import name,system
from sys import stdout
from concurrent.futures import ThreadPoolExecutor
from threading import Thread,Lock,active_count
from string import ascii_letters,digits
import json
import requests
from selenium.common.exceptions import NoSuchElementException

class Main:
    def clear(self):
        if name == 'posix':
            system('clear')
        elif name in ('ce', 'nt', 'dos'):
            system('cls')
        else:
            print("\n") * 120

    def SetTitle(self,title_name:str):
        system("title {0}".format(title_name))
        
    def GetRandomUserAgent(self):
        useragents = self.ReadFile('useragents.txt','r')
        return choice(useragents)

    def PrintText(self,bracket_color:Fore,text_in_bracket_color:Fore,text_in_bracket,text):
        self.lock.acquire()
        stdout.flush()
        text = text.encode('ascii','replace').decode()
        stdout.write(Style.BRIGHT+bracket_color+'['+text_in_bracket_color+text_in_bracket+bracket_color+'] '+bracket_color+text+'\n')
        self.lock.release()

    def GetRandomProxyForStream(self):
        proxies_file = self.ReadFile('streaming_http_proxies.txt','r')
        return choice(proxies_file)

    def GetRandomProxyForAccountCreator(self):
        proxies_file = self.ReadFile('account_creator_proxies.txt','r')
        proxies = {}
        if self.proxy_type == 1:
            proxies = {
                "http":"http://{0}".format(choice(proxies_file)),
                "https":"https://{0}".format(choice(proxies_file))
            }
        elif self.proxy_type == 2:
            proxies = {
                "http":"socks4://{0}".format(choice(proxies_file)),
                "https":"socks4://{0}".format(choice(proxies_file))
            }
        else:
            proxies = {
                "http":"socks5://{0}".format(choice(proxies_file)),
                "https":"socks5://{0}".format(choice(proxies_file))
            }
        return proxies
        

    def ReadFile(self,filename,method):
        with open(filename,method) as f:
            content = [line.strip('\n') for line in f]
            return content

    def AddRandomDomain(self,username):
        email_providers = ['gmail.com', 'yahoo.com', 'hotmail.com', 'hotmail.co.uk', 'hotmail.fr', 'outlook.com', 'icloud.com', 'mail.com', 'live.com', 'yahoo.it', 'yahoo.ca', 'yahoo.in', 'live.se', 'orange.fr', 'msn.com', 'mail.ru', 'mac.com']
        return username+'@'+choice(email_providers)

    def GenCredentails(self):
        credentails = {}
        credentails['gender'] = 'male'
        credentails['birth_year'] = randint(1970,2005)
        credentails['birth_month'] = randint(1,12)
        credentails['birth_day'] = randint(1,28)
        password_characters = ascii_letters + digits
        password_characters = 'Hz5QhfUBEnU6vfT'
        credentails['password'] = password_characters
        username = ascii_letters + digits
        username = ''.join(choice(username) for i in range(randint(7,11)))
        credentails['username'] = username
        email = self.AddRandomDomain(username)
        credentails['email'] = email
        return credentails
            

    def __init__(self):
        init(convert=True)
        self.lock = Lock()
        self.clear()
        self.SetTitle('One Man Builds Spotify Streaming Tool Selenium')
        self.title = Style.BRIGHT+Fore.RED+"""
                                    ╔══════════════════════════════════════════════════╗
                                       ╔═╗╔═╗╔═╗╔╦╗╦╔═╗╦ ╦  ╔═╗╔╦╗╦═╗╔═╗╔═╗╔╦╗╦╔╗╔╔═╗
                                       ╚═╗╠═╝║ ║ ║ ║╠╣ ╚╦╝  ╚═╗ ║ ╠╦╝║╣ ╠═╣║║║║║║║║ ╦
                                       ╚═╝╩  ╚═╝ ╩ ╩╚   ╩   ╚═╝ ╩ ╩╚═╚═╝╩ ╩╩ ╩╩╝╚╝╚═╝
                                    ╚══════════════════════════════════════════════════╝                                                           
                                                                                                
        """
        print(self.title)
        self.method = 1
        self.stream_type = 2
        self.use_proxy = 2
        
        if self.use_proxy == 1 and self.method != 1:
            self.proxy_type = int(input(Style.BRIGHT+Fore.CYAN+'['+Fore.RED+'>'+Fore.CYAN+'] ['+Fore.RED+'1'+Fore.CYAN+']Https ['+Fore.RED+'2'+Fore.CYAN+']Socks4 ['+Fore.RED+'3'+Fore.CYAN+']Socks5: '))

        self.minplay = 190
        self.maxplay = 190
        self.number_of_songs = 50
        self.browser_amount = 1
        self.max_wait = 10
        self.website_load_max_wait = 10
        self.login_check_max_wait = 10
        self.wait_before_start = 10
        self.url = str(input(Style.BRIGHT+Fore.CYAN+'['+Fore.RED+'>'+Fore.CYAN+'] Stream url: '))
        print('')


    def SpotifyCreator(self):
        try:
            create_headers = {
             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0',
             'Accept': '*/*',
             'Accept-Language': 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3',
             'Accept-Encoding': 'gzip, deflate, br',
             'Content-Type': 'application/json',
             'Origin': 'https://www.spotify.com',
             'Sec-Fetch-Dest': 'empty',
             'Sec-Fetch-Mode': 'no-cors',
             'Sec-Fetch-Site': 'same-site',
             'Referer': 'https://www.spotify.com/',
             'Connection': 'keep-alive',
             'Pragma': 'no-cache',
             'Cache-Control': 'no-cache'
            }

            create_response = ''

            create_url = 'https://spclient.wg.spotify.com/signup/public/v2/account/create'
            

            credentails = self.GenCredentails()
            
            payload=f"{{\r\n    \"account_details\": {{\r\n        \"birthdate\": \"1989-06-12\",\r\n        \"consent_flags\": {{\r\n            \"eula_agreed\": true,\r\n            \"send_email\": false,\r\n            \"third_party_email\": false\r\n        }},\r\n        \"display_name\": \"nabiilspoty\",\r\n        \"email_and_password_identifier\": {{\r\n            \"email\": \"{credentails['email']}\",\r\n            \"password\": \"Hz5QhfUBEnU6vfT\"\r\n        }},\r\n        \"gender\": 1\r\n    }},\r\n    \"callback_uri\": \"https://www.spotify.com/signup/challenge?forward_url=https%3A%2F%2Fopen.spotify.com%2F&locale=fr\",\r\n    \"client_info\": {{\r\n        \"api_key\": \"a1e486e2729f46d6bb368d6b2bcda326\",\r\n        \"app_version\": \"v2\",\r\n        \"capabilities\": [\r\n            1\r\n        ],\r\n        \"installation_id\": \"5e10d26f-8843-422e-afd6-7ce417dd8eb5\",\r\n        \"platform\": \"www\"\r\n    }},\r\n    \"tracking\": {{\r\n        \"creation_flow\": \"\",\r\n        \"creation_point\": \"https://www.spotify.com/fr/\",\r\n        \"referrer\": \"\"\r\n    }}\r\n}}"
            create_response = ''


            if self.use_proxy == 1:
                create_response = requests.post(create_url, data=payload, headers=create_headers,proxies=self.GetRandomProxyForAccountCreator(),timeout=5)
            else:
                create_response = requests.post(create_url, data=payload, headers=create_headers)

            json_data = json.loads(create_response.text)

            if json_data['success'] is not None:
                username = json_data['success']['username']
                if username != '':
                        self.PrintText(Fore.CYAN,Fore.RED,'CREATED','{0}:{1} | {2} | {3} | {4}/{5}/{6}'.format(credentails['email'],credentails['password'],credentails['username'],credentails['gender'],credentails['birth_year'],credentails['birth_month'],credentails['birth_day']))
                        if self.method != 1:
                            self.StartStream(credentails['email'],credentails['password'])
                else:
                     self.SpotifyCreator()
            else:
                self.SpotifyCreator()            
        except:
            self.SpotifyCreator()

    def Login(self,username,password,driver):
        try:
            logged_in = False

            driver.get('https://accounts.spotify.com/en/login/')

            sleep(7)
            login_username_present = EC.presence_of_element_located((By.ID, 'login-username'))
            WebDriverWait(driver, self.website_load_max_wait).until(login_username_present)

            username_elem = driver.find_element_by_id('login-username').send_keys(username)
            password_elem = driver.find_element_by_id('login-password').send_keys(password)
            login_button_elem = driver.find_element_by_id('login-button').click()


            try:
                url_to_be_present = EC.url_to_be('https://accounts.spotify.com/en/status')
                WebDriverWait(driver, self.login_check_max_wait).until(url_to_be_present)
                self.PrintText(Fore.CYAN,Fore.RED,'LOGIN',f'LOGGED IN WITH | {username}:{password}')
                logged_in = True
            except TimeoutException:
                self.PrintText(Fore.RED,Fore.CYAN,'LOGIN',f'FAILED TO LOGIN WITH | {username}:{password}')
                logged_in = False
        
            return logged_in
        except Exception as e:
            print(e)
            driver.quit()
            self.Login(username,password,driver)

    def StreamArtist(self,username,password):
        try:
            options = Options()

            options.add_argument(f'--user-agent={self.GetRandomUserAgent()}')
            options.add_argument('--no-sandbox')
            options.add_argument('--log-level=3')
            options.add_argument('--lang=en')

            if self.use_proxy == 1:
                options.add_argument('--proxy-server=http://{0}'.format(self.GetRandomProxyForStream()))

            #Removes navigator.webdriver flag
            options.add_experimental_option('excludeSwitches', ['enable-logging','enable-automation'])
            
            # For older ChromeDriver under version 79.0.3945.16
            options.add_experimental_option('useAutomationExtension', False)

            options.add_argument("window-size=1280,800")

            #For ChromeDriver version 79.0.3945.16 or over
            options.add_argument('--disable-blink-features=AutomationControlled')
            driver = webdriver.Chrome(options=options)

            if self.Login(username,password,driver) == True:
                driver.get(self.url)
                element_present = EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div/div[2]/div[4]/main/div/div[2]/div/div/div[2]/section/div/div[4]/div[1]/div/div/div/div[2]/div[1]/div/div/div[1]'))
                WebDriverWait(driver, self.max_wait).until(element_present)
                index = 0
                for i in range(self.number_of_songs):
                    index += 1
                    playtime = randint(self.minplay,self.maxplay)
                    WebDriverWait(driver,self.max_wait).until(EC.element_to_be_clickable((By.XPATH,f'/html/body/div[4]/div/div[2]/div[4]/main/div/div[2]/div/div/div[2]/section/div/div[4]/div[1]/div/div/div/div[2]/div[{index}]/div/div/div[1]'))).click()
                    WebDriverWait(driver,self.max_wait).until(EC.text_to_be_present_in_element((By.XPATH,'/html/body/div[4]/div/div[2]/div[3]/footer/div[1]/div[2]/div/div[2]/div[1]'),'0:01'))
                    sleep(playtime)
                    self.PrintText(Fore.CYAN,Fore.RED,'ARTIST STREAM',f'SONG {index} | STREAMED FOR {playtime}s | WITH {username}:{password}')
        except Exception as e:
            print(e)
            driver.quit()
            self.StreamArtist(username,password)
        finally:
            driver.quit()

    def StreamPlaylistOrAlbum(self,username,password):
        try:
            options = Options()

            options.add_argument(f'--user-agent={self.GetRandomUserAgent()}')
            options.add_argument('--no-sandbox')
            options.add_argument('--log-level=3')
            options.add_argument('--lang=en')

            if self.use_proxy == 1:
                options.add_argument('--proxy-server=http://{0}'.format(self.GetRandomProxyForStream()))

            #Removes navigator.webdriver flag
            options.add_experimental_option('excludeSwitches', ['enable-logging','enable-automation'])
            
            # For older ChromeDriver under version 79.0.3945.16
            options.add_experimental_option('useAutomationExtension', False)

            options.add_argument("window-size=1280,800")

            #For ChromeDriver version 79.0.3945.16 or over
            options.add_argument('--disable-blink-features=AutomationControlled')
            driver = webdriver.Chrome(options=options)

            if self.Login(username,password,driver) == True:
                driver.get(self.url)
                sleep(5)
                try:
                    cookie_check = driver.find_element_by_id('onetrust-accept-btn-handler')
                    if len(cookie_check) > 0:
                       cookie_check.click()
                except NoSuchElementException:
                    print("fail")
                print("1")
                WebDriverWait(driver,self.max_wait).until(EC.element_to_be_clickable((By.XPATH,"//div[@data-testid='action-bar-row']/div[@class='PFgcCoJSWC3KjhZxHDYH']/button[@data-testid='play-button']"))).click()
                print("2")
                realplaytime = driver.find_element_by_class_name('Btg2qHSuepFGBG6X0yEN').text
                print(realplaytime)
                playtime = randint(self.minplay,self.maxplay)
                sleep(playtime)
                self.PrintText(Fore.CYAN,Fore.RED,'PLAYLIST OR ALBUM STREAM',f'SONG | STREAMED FOR {realplaytime}s | WITH {username}:{password}')

        except Exception as e:
            print(e)
            driver.quit()
            self.StreamPlaylistOrAlbum(username,password)
        finally:
            driver.quit()

    def StartStream(self,username,password):
        if self.stream_type == 1:
            self.StreamArtist(username,password)
        else:
            self.StreamPlaylistOrAlbum(username,password)

    def Start(self):
            if self.method == 1:
                combos = self.ReadFile('combos.txt','r')
                with ThreadPoolExecutor(max_workers=self.browser_amount) as ex:
                    for combo in combos:
                        username = combo.split(':')[0]
                        password = combo.split(':')[-1]
                        ex.submit(self.StartStream,username,password)
                        if self.wait_before_start > 0:
                            sleep(self.wait_before_start)
            else:
                while True:
                    if active_count()<= self.browser_amount:
                        Thread(target=self.SpotifyCreator).start()
                        if self.wait_before_start > 0:
                            sleep(self.wait_before_start)
                
if __name__ == "__main__":
    main = Main()
    main.Start()
    
