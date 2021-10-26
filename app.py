from flask import Flask , render_template
from country_codes import country_dict
app = Flask(__name__)
# https://flagpedia.net/download/api
@app.route("/", methods = ["GET"])
def home():
    flag_url = f"https://flagcdn.com/w320/{country_dict.popitem()[0]}.jpg"
    return render_template("index.html",flag_url=flag_url)

if __name__ == "__main__":
    app.run(debug = True)
