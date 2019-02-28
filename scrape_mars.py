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
    url2 = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    # Retrieve page with the requests module
    browser.visit(url2)
    # Create BeautifulSoup object; parse with 'lxml'
    html2 = browser.html
    soup2 = BeautifulSoup(html2, 'html.parser')
    #retrieve image from website
    item = soup2.find('a', class_='fancybox')
    featured_img = item['data-fancybox-href'] 
    featured_image_url = url2 + featured_img          

    #print(featured_img)
    #print(featured_img_url)


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
    #pulling hemispheres 
    hemispheres_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(hemispheres_url)
  
    
    html7 = browser.html
    soup7 = BeautifulSoup(html7, "html.parser")

    mars_hemisphere = []
    products = soup7.find("div", class_ = "result-list" )
    hemispheres = products.find_all("div", class_="item")
    for hemisphere in hemispheres:
        title = hemisphere.find("h3").text
        title = title.replace("Enhanced", "")
        end_link = hemisphere.find("a")["href"]
        
        image_link = "https://astrogeology.usgs.gov/" + end_link    
        
        browser.visit(image_link)
        html8 = browser.html
        soup8=BeautifulSoup(html8, "html.parser")
        
        downloads = soup8.find("div", class_="downloads")
        image_url = downloads.find("a")["href"]
        mars_hemisphere.append({"title": title, "img_url": image_url})

    #dictionary holding variables
    mars_scrape_data = {
        'news_title': news_title, #title
        'news_p': news_p, #paragraph
        'featured_image_url': featured_image_url, #pic
        'mars_weather': mars_weather, #twitter
        'mars_hemisphere': mars_hemisphere
    }

    return mars_scrape_data
