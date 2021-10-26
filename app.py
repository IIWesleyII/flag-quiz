'''
Web app that challenges your knowledge of flags.
    - Flag will appear on screen, you must select a button 
    with the country that corresponds to that flag.
'''
from flask import Flask , render_template,request
from country_codes import country_dict
import random
app = Flask(__name__)

'''
global variables
     int correct - correct flag guesses
     int incorrect- incorrect flag guesses
     tuple country - country is in the form ("US","United States")
'''
correct, incorrect, country = 0, 0, (None,None)

@app.route("/", methods = ["GET","POST"])
def home():
    global correct, incorrect, country

    if request.method == 'POST' and None not in country:
        if "RESET" in request.form:
            correct, incorrect = 0, 0  
        elif country[1] in request.form:
            correct += 1
        else:
            incorrect += 1
    '''
    Generate a list of 4 random countries, including the one that corresponds to the flag displayed
    List will be rendered as buttons for the user to select from
    '''
    country = random.choice(list(country_dict.items()))
    flag_url = f"https://flagcdn.com/w320/{country[0]}.jpg"
    country_list = []
    country_list.append(country[1])
    for i in range(3):
        country_list.append(random.choice(list(country_dict.items()))[1])
    random.shuffle(country_list)

    return render_template("index.html",flag_url=flag_url,country_list=country_list,correct=correct,incorrect=incorrect)

if __name__ == "__main__":
    app.run(debug = True)
