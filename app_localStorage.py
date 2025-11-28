from flask import Flask, render_template, jsonify
import os

app = Flask(__name__)

# Simple backend - just serves the HTML
# All data stored on user's phone in localStorage!

@app.route('/')
def index():
    return render_template('index.html')

# Health check endpoint
@app.route('/health')
def health():
    return jsonify({'status': 'ok', 'storage': 'localStorage on client device'})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
