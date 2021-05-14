`Forked from Konyanj0278's checkout tool, repurposed to work on amazon(IN) for ps5`

## Amazon-Automated-Checkout
---
A bot repurposed to constantly run and purchase an item on Amazon.in, built to help friends and family get their console of choice (configured for PS5).
--

  <br/>

### From the original creator
-------------------------

Update 1/21

Since creating this bot BestBuy has changed the its checkout process to where human verification is required, as I am a student I have not had the chance to update the bot to circumvent this. I will post updates when possible. Thank you for all the support.

Hello all,

I created this bot to help me get a new RTX 30 series graphics card through BestBuy. I was able to get the card and now want to share this bot with everyone.

Requirements:\
 Selenium\
 Tkinter\
 Chrome webdriver
 
Orginal Release v1.0:\
With this intial release the code does work as of 11/4/20 and is able to purchase any item that registers as in stock on the BestBuy website. It does require that you give the SKU number of the item you are trying to get. This is easily avaialbe on the products webpage.
  
  
How to use:

1) Make sure that all required libraries are installed.
2) Rename the "config_" file to "config".
3) Save the Chrome webdriver in the same directory as BestBuybot.py
4) Open the config file with a text editor and fill in the parrameters with your information, if you are an employee of BestBuy there    is a field for your employee number.
5) Edit the code and change the field of bot.searctag() to contain the sku that you want, do note that this field takes a string and    not an integer. 
6) Run bot and Enjoy


Link to latest version of ChromeWebdriver:
https://chromedriver.chromium.org/downloads
