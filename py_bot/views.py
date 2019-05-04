from flask import Flask, render_template, request, jsonify
import py_bot.utils as utils
import py_bot.config as id_g


app = Flask(__name__)


@app.before_request
def before_request():
    if 'localhost' in request.host_url or '0.0.0.0' in request.host_url:
        app.jinja_env.cache = {}


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', api_key=id_g.KEY)


@app.route('/_google_map', methods=['GET'])
def google_map():
    user_search = request.args.get('user_search', '')
    try:
        lat, lng, address = utils.get_map(user_search)
        return jsonify(lat, lng, address)
    except ValueError:
        return jsonify('Error')


@app.route('/_wiki', methods=['GET'])
def wiki():
    address = request.args.get('address', '')
    word = utils.format_response(address)
    result = utils.get_section(word)
    return jsonify(result)


