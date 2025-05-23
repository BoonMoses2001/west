import os
from flask import Flask, render_template

# Create the app
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "westcoast-digital-denture-secret-key-2024")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/all-on-x')
def all_on_x():
    return render_template('all_on_x.html')

@app.route('/partial-dentures')
def partial_dentures():
    return render_template('partial_dentures.html')

@app.route('/full-dentures')
def full_dentures():
    return render_template('full_dentures.html')

@app.errorhandler(404)
def not_found(error):
    return render_template('index.html'), 200

@app.errorhandler(500)
def internal_error(error):
    return render_template('index.html'), 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)