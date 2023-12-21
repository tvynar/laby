import os
import requests
from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def display_website_content():
    # Отримуємо вміст веб-сторінки
    response = requests.get('https://httpbin.org/')
    website_content = response.text

    # Відображаємо вміст на сторінці Flask
    template = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Website Content</title>
    </head>
    <body>
        <h1>Website Content</h1>
        <pre>{{ website_content }}</pre>
    </body>
    </html>
    """
    return render_template_string(template, website_content=website_content)

if __name__ == '__main__':
    app.run(debug=True)