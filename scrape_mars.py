from splinter import Browser
from bs4 import BeautifulSoup
#import requests

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)


def scrape():
    browser = init_browser()
   

    url = 'https://mars.nasa.gov/news/'
    
    # Retrieve page with the requests module
    browser.visit(url)
    # Create BeautifulSoup object; parse with 'lxml'
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    # Retrieve divs for the first article
    article_result = soup.find('div', class_='content_title')
    news_title = article_result.text   
    ##print(news_title) 
    #Retrieve the descripton of  first article 
    paragraph_result= soup.find('div', class_='rollover_description_inner')
    news_p = paragraph_result.text
    ##print(news_p)


    #  URL of page to be scraped
    url2 = 'https://www.jpl.nasa.gov/spaceimages/details.php?id=PIA19871'
    # Retrieve page with the requests module
    browser.visit(url2)
    # Create BeautifulSoup object; parse with 'lxml'
    html2 = browser.html
    soup2 = BeautifulSoup(html2, 'html.parser')
    #retrieve image from website
    image_result = soup2.find('figure', class_='lede')
    featured_image_url = image_result.a['href']
    ##print('http://www.jpl.nasa.gov' + featured_image_url)


    # URL of page to be scraped
    url3= 'https://twitter.com/marswxreport?lang=en'
    # Retrieve page with the requests module
    browser.visit(url3)
    # Create BeautifulSoup object; parse with 'lxml'\
    html3 = browser.html
    soup3 = BeautifulSoup(html3, 'html.parser')
    #Retrieve most recent tweet 
    tweets = soup3.find('p', class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text')
    mars_weather = tweets.text
    #print(mars_weather)


    ##Mars Hemispheres
    mars_scrape_data = {
        'news_title': news_title, #title
        'news_p': news_p, #paragraph
        'featured_image_url': featured_image_url,
        'mars_weather': mars_weather
    }

    return mars_scrape_data
