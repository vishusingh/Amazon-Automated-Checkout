#%%
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
import urllib.request
import os
from configparser import ConfigParser
import tkinter as tk

class BBYbot():
  def __init__(self,config):

    self.driver = webdriver.Chrome('./chromedriver')
    self.url="https://www.amazon.in/"
    self.username=config.get('BBY_ACCOUNT','USERNAME')
    self.password=config.get('BBY_ACCOUNT','PASSWORD')
    self.ID=config.get('BBY_ACCOUNT','ID')
    self.card=config.get('CARD_INFO','CARD#')
    self.cardsecurity=config.get('CARD_INFO','CARDSECURITY')
    self.expm=config.get('CARD_INFO','EXPM')
    self.expy=config.get('CARD_INFO','EXPY')
    self.cvv=config.get('CARD_INFO','CVV')
  

    self.driver.get(self.url)

  def Login(self):
    self.driver.find_element_by_css_selector("a#nav-link-accountList").click()
    time.sleep(2)
    username_input=self.driver.find_element_by_xpath('//*[@id="ap_email"]')
    username_input.send_keys(self.username)
    self.driver.find_element_by_class_name("a-button-input").click()
    password_input = self.driver.find_element_by_xpath('//*[@id="ap_password"]')
    password_input.send_keys(self.password)
    password_input.submit()
    time.sleep(2)

    try:
      employee=self.driver.find_element_by_xpath('/html/body/div[1]/div/section/main/div[1]/div/div/div/div/form/div[1]/div/input')
      employee.send_keys(self.ID)
      employee.submit()
    except:
      return

  def navtoProd(self):
    self.driver.get('https://www.amazon.in/gp/product/B08FV5GC28/ref=s9_acss_bw_cg_button_2a1_w?pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-1&pf_rd_r=X3DVWGP1TW3DA5SVRY7M&pf_rd_t=101&pf_rd_p=01e9c541-42d0-4ab7-ba81-f69fbb14851b&pf_rd_i=21725163031')

  def in_stock(self):
    time.sleep(2)
    try:
      item = self.driver.find_element_by_id('submit.add-to-cart-announce')
      print("In stock!")
      return True

    except:
      self.driver.refresh()
      time.sleep(3)
      print("Item is out of stock - retrying...")
      return False

  def add_toCart(self, incart):
    try:
      time.sleep(2)
      item =self.driver.find_element_by_id('add-to-cart-button')
      item.click()
      time.sleep(2)				
      go_to_cart_button= self.driver.find_element_by_id("nav-cart")
      
      go_to_cart_button.click()
      incart=True
      return incart
      
    except:
      print("Couldnt add to cart trying again")
      incart=False
  def checkout(self):
    time.sleep(2)
    #starts checkout
    self.driver.find_element_by_id('sc-buy-box-ptc-button').click()
    #selects address
    time.sleep(2)
    self.driver.find_element_by_css_selector('#address-book-entry-0 .ship-to-this-address').click()
    #continues to payment
    time.sleep(2)
    self.driver.find_element_by_xpath('/html/body/div[5]/div[1]/div/div[2]/div/div[1]/form/div[1]/div[2]/div/span[1]/span/input').click()
    time.sleep(2)
    # Entering cvv and proceeding to the final step
    cvvInput = self.driver.find_element_by_css_selector('.pmts-selected .a-input-text')
    cvvInput.send_keys(self.cvv)
    time.sleep(.5)
    self.driver.find_element_by_xpath('/html/body/div[5]/div[1]/div[2]/div[3]/div/div[2]/div[1]/form/div[2]/div/div/div/span/span/input').click()
    time.sleep(10)

  def closeEmailprompt(self):
    self.driver.find_element_by_class_name("c-modal-close-icon").click()
  def close(self):
    self.driver.close()

print("Starting Bot")
searchtag=''
config_file= ConfigParser()
config_file.read("config.ini")
bot = BBYbot(config_file)
try:
  time.sleep(1)
  bot.Login()
except:
  bot.closeEmailprompt()
  time.sleep(3)
  bot.Login()
time.sleep(1)
bot.navtoProd()
instock= bot.in_stock()
incart=False
# driver = webdriver.Chrome('./chromedriver')
while(instock!=True) :
  instock = bot.in_stock()

if (instock==True) :
  while(incart != True):
    incart=bot.add_toCart(incart)
    print("In cart!")
time.sleep(1)
bot.checkout()

print("compiled")
bot.close()

# %%
