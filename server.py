from flask import Flask, render_template, make_response, send_from_directory
from os import environ, chdir, listdir
from os.path import abspath, dirname
from random import choice
from base64 import b64encode

app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = environ.get("SECRET_KEY", "".join(choice("abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)") for _ in range(50)))


@app.route('/', methods=['GET'])
def index():

    barcodes_dict = {
        'lenta': "data:image/png;base64," + b64encode(open(f'./static/images/codes/lenta/{choice(listdir(abspath("./static/images/codes/lenta/")))}', 'rb').read()).decode("utf-8").strip("b"),
        'ostin': "data:image/png;base64," + b64encode(open(f'./static/images/codes/ostin/{choice(listdir(abspath("./static/images/codes/ostin/")))}', 'rb').read()).decode("utf-8").strip("b"),
        'restore': "data:image/png;base64," + b64encode(open(f'./static/images/codes/restore/{choice(listdir(abspath("./static/images/codes/restore/")))}', 'rb').read()).decode("utf-8").strip("b"),
        'advantage': "data:image/png;base64," + b64encode(open(f'./static/images/codes/advantage/{choice(listdir(abspath("./static/images/codes/advantage/")))}', 'rb').read()).decode("utf-8").strip("b"),
        '585gold': "data:image/png;base64," + b64encode(open(f'./static/images/codes/585gold/{choice(listdir(abspath("./static/images/codes/585gold/")))}', 'rb').read()).decode("utf-8").strip("b"),
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


@app.route('/fonts/<path:path>', methods=['GET'])
def serve_fonts(path):
    return send_from_directory('static/fonts', path)


if __name__ == "__main__":
    chdir(dirname(abspath(__file__)))
    app.run(debug=False, use_reloader=True)
