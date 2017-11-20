from flask import Flask, render_template, make_response, send_from_directory
from flask_sslify import SSLify
from os import environ, chdir, listdir
from os.path import abspath, dirname
from random import choice
from base64 import b64encode


debug = False
app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = environ.get("SECRET_KEY", "".join(choice("abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)") for _ in range(50)))

if not debug:
    sslify = SSLify(app)


@app.route('/', methods=['GET'])
def index():

    barcodes_dict = {
        'lenta': "data:image/png;base64," + b64encode(open(f'./static/images/codes/lenta/{choice(listdir(abspath("./static/images/codes/lenta/")))}', 'rb').read()).decode("utf-8").strip("b"),
        'ostin': "data:image/png;base64," + b64encode(open(f'./static/images/codes/ostin/{choice(listdir(abspath("./static/images/codes/ostin/")))}', 'rb').read()).decode("utf-8").strip("b"),
        'restore': "data:image/png;base64," + b64encode(open(f'./static/images/codes/restore/{choice(listdir(abspath("./static/images/codes/restore/")))}', 'rb').read()).decode("utf-8").strip("b"),
        'advantage': "data:image/png;base64," + b64encode(open(f'./static/images/codes/advantage/{choice(listdir(abspath("./static/images/codes/advantage/")))}', 'rb').read()).decode("utf-8").strip("b"),
        '585gold': "data:image/png;base64," + b64encode(open(f'./static/images/codes/585gold/{choice(listdir(abspath("./static/images/codes/585gold/")))}', 'rb').read()).decode("utf-8").strip("b"),
        'sony': "data:image/png;base64," + b64encode(open(f'./static/images/codes/sony/{choice(listdir(abspath("./static/images/codes/sony/")))}', 'rb').read()).decode("utf-8").strip("b"),
        'samsung': "data:image/png;base64," + b64encode(open(f'./static/images/codes/samsung/{choice(listdir(abspath("./static/images/codes/samsung/")))}', 'rb').read()).decode("utf-8").strip("b"),
        'funday': "data:image/png;base64," + b64encode(open(f'./static/images/codes/funday/{choice(listdir(abspath("./static/images/codes/funday/")))}', 'rb').read()).decode("utf-8").strip("b"),
        'nike': "data:image/png;base64," + b64encode(open(f'./static/images/codes/nike/{choice(listdir(abspath("./static/images/codes/nike/")))}', 'rb').read()).decode("utf-8").strip("b"),
        'evrasia': "data:image/png;base64," + b64encode(open(f'./static/images/codes/evrasia/{choice(listdir(abspath("./static/images/codes/evrasia/")))}', 'rb').read()).decode("utf-8").strip("b"),
        'eldorado': "data:image/png;base64," + b64encode(open(f'./static/images/codes/eldorado/{choice(listdir(abspath("./static/images/codes/eldorado/")))}', 'rb').read()).decode("utf-8").strip("b"),
        '4itay_gorod': "data:image/png;base64," + b64encode(open(f'./static/images/codes/4itay_gorod/{choice(listdir(abspath("./static/images/codes/4itay_gorod/")))}', 'rb').read()).decode("utf-8").strip("b"),
        '5tero4ka': "data:image/png;base64," + b64encode(open(f'./static/images/codes/5tero4ka/{choice(listdir(abspath("./static/images/codes/5tero4ka/")))}', 'rb').read()).decode("utf-8").strip("b"),
        'adidas': "data:image/png;base64," + b64encode(open(f'./static/images/codes/adidas/{choice(listdir(abspath("./static/images/codes/adidas/")))}', 'rb').read()).decode("utf-8").strip("b"),
        'burger_king': "data:image/png;base64," + b64encode(open(f'./static/images/codes/burger_king/{choice(listdir(abspath("./static/images/codes/burger_king/")))}', 'rb').read()).decode("utf-8").strip("b"),
        'carusel': "data:image/png;base64," + b64encode(open(f'./static/images/codes/carusel/{choice(listdir(abspath("./static/images/codes/carusel/")))}', 'rb').read()).decode("utf-8").strip("b"),
        'cinema_park': "data:image/png;base64," + b64encode(open(f'./static/images/codes/cinema_park/{choice(listdir(abspath("./static/images/codes/cinema_park/")))}', 'rb').read()).decode("utf-8").strip("b"),
        'fixprice': "data:image/png;base64," + b64encode(open(f'./static/images/codes/fixprice/{choice(listdir(abspath("./static/images/codes/fixprice/")))}', 'rb').read()).decode("utf-8").strip("b"),
        'maxidom': "data:image/png;base64," + b64encode(open(f'./static/images/codes/maxidom/{choice(listdir(abspath("./static/images/codes/maxidom/")))}', 'rb').read()).decode("utf-8").strip("b"),
        'mediamarkt': "data:image/png;base64," + b64encode(open(f'./static/images/codes/mediamarkt/{choice(listdir(abspath("./static/images/codes/mediamarkt/")))}', 'rb').read()).decode("utf-8").strip("b"),
        'mvideo': "data:image/png;base64," + b64encode(open(f'./static/images/codes/mvideo/{choice(listdir(abspath("./static/images/codes/mvideo/")))}', 'rb').read()).decode("utf-8").strip("b"),
        'okey': "data:image/png;base64," + b64encode(open(f'./static/images/codes/okey/{choice(listdir(abspath("./static/images/codes/okey/")))}', 'rb').read()).decode("utf-8").strip("b")
    }

    response = make_response(render_template("index.html", barcodes=barcodes_dict))

    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    response.headers['Cache-Control'] = 'no-cache'
    response.headers['Strict-Transport-Security'] = 'max-age=31536000'

    return response


@app.route('/images/<path:path>', methods=['GET'])
def serve_images(path):
    return send_from_directory('static/images', path)


@app.route('/images/thumbs/<path:path>', methods=['GET'])
def serve_thumbs(path):
    return send_from_directory('static/images/thumbs', path)


@app.route('/js/<path:path>', methods=['GET'])
def serve_js(path):
    return send_from_directory('static/js', path)


@app.route('/css/<path:path>', methods=['GET'])
def serve_css(path):
    return send_from_directory('static/css', path)


@app.route('/config/<path:path>', methods=['GET'])
def serve_config(path):
    return send_from_directory('static/config', path)


@app.route('/fonts/<path:path>', methods=['GET'])
def serve_fonts(path):
    return send_from_directory('static/fonts', path)


if __name__ == "__main__":
    chdir(dirname(abspath(__file__)))
    app.run(debug=debug, use_reloader=True)
