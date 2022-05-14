from flask import Flask, render_template, request
import os
import string
app = Flask(__name__)

############ APP OVERVIEW ########
# index.html (Welcome page) -> long_url generate page
# short url -> redirect page
# 404errr
##################################
BASE62 = string.digits + string.ascii_letters

# index is our home
# flow: index -> generated_shorturl
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_shorturl', methods = ['POST'])
def generate_shorturl():
    #long_url = request.args.get("long_url")
    print(request.form)
    short_url = get_short_url()
    return render_template(
        'generated_shorturl.html',
        short_url=short_url
    )
# http://2gzyxa5ihm7nsggfxnu52rck2vv4rvmdlkiu3zzui5du4xyclen53wid.onion/index.html

def get_short_url():
    random_num = os.urandom(16)
    short_url = ''
    while random_num!=0:
        short_url += BASE62[random_num%62]
    return short_url
    
@app.route('/<short_url>')
def redirect(short_url):
    long_url = short_url
    return render_template(
        'redirect_template.html',
        long_url = long_url,
        short_url = short_url,
    )

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=False, port=8080)