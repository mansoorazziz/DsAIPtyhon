from flask import Flask
app = Flask(__name__)

# route for home page
@app.route('/')
def hello_world():
    return 'Hello, World!'

# route for about page
@app.route('/about')
def about():
    return 'About Page'

# route for contact page
@app.route('/contact')
def contact():
    return '<h1>Contact Page</h1><p>You can contact us at contact@example.com</p>'

if __name__ == '__main__':
    app.run(debug=True)
