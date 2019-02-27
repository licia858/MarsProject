from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars  #need the name of all the scrapes without the py

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

@app.route("/")
def home():

    mars_data = mongo.db.collection.find_one()

    return render_template("index.html", mars_listing=mars_data)



@app.route("/scrape")
def scrape():
    #Run scrape function
    marsmars = scrape_mars.scrape()
    #update mongo database with update data
    mongo.db.collection.update({}, marsmars, upsert=True)
    
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)