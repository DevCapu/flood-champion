from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


class Main():

    def __init__(self):
        self.driver = webdriver.Firefox()

    def login(self):
        self.driver.get("https://discord.com/app")

        input_email = self.driver.find_element_by_xpath(
            "/html/body/div/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/div[1]/div/input")

        input_email.send_keys("SEU EMAIL AQUI!!!")

        input_password = self.driver.find_element_by_xpath(
            "/html/body/div/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/div[2]/div/input")
        input_password.send_keys("SUA SENHA AQUI!!!!")

        login_button = self.driver.find_element_by_xpath(
            "/html/body/div/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/button[2]")
        login_button.click()

        sleep(10)

        # NA LINHA DE BAIXO ONDE ESTÁ O 5 TROCAR PELA POSIÇÃO DO SERVIDOR QUE VC QUER MANDAR A MENSAGEM
        servidorDaBizi = self.driver.find_element_by_css_selector("div.listItem-2P_4kh:nth-child(5)")
        servidorDaBizi.click()
        sleep(3)

        # NA LINHA DE BAIXO ONDE ESTÁ O 7 TROCAR PELA POSIÇÃO DO CANAL QUE VC QUER MANDAR A MENSAGEM
        canalDeFlood = self.driver.find_element_by_css_selector("div.containerDefault-1ZnADq:nth-child(7)")
        canalDeFlood.click()

        while (True):
            input = self.driver.find_element_by_css_selector(".slateTextArea-1Mkdgw")
            input.send_keys("up")
            input.send_keys(Keys.RETURN)
            sleep(61)


bot = Main()
bot.login()
