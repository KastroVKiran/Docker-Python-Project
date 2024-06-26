from flask import Flask, render_template_string
import os

app = Flask(__name__)

@app.route("/")
def hello():
    html_content = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Docker Course</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                height: 100vh;
                margin: 0;
                background-color: #f4f4f4;
            }
            .container {
                text-align: center;
                background: #fff;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            }
            .header {
                display: flex;
                justify-content: space-between;
                align-items: center;
                width: 100%;
                max-width: 600px;
                margin-bottom: 20px;
            }
            .header img {
                border-radius: 50%;
                width: 80px;
                height: 80px;
            }
            .title {
                color: #0044cc;
                font-weight: bold;
                font-size: 24px;
            }
            .subtitle {
                font-style: italic;
                color: #ff6600;
                font-weight: bold;
            }
            .button {
                display: inline-block;
                padding: 10px 20px;
                margin: 10px;
                font-size: 16px;
                color: #fff;
                text-decoration: none;
                border-radius: 5px;
            }
            .docker-button {
                background-color: #0db7ed;
            }
            .linkedin-button {
                background-color: #0077b5;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <div>
                    <div class="title">Docker - Basics to Brilliance Course</div>
                    <div class="subtitle">by <span style="color: #ff6600;">Kastro Kiran V</span></div>
                </div>
                <img src="https://media.licdn.com/dms/image/D5603AQHJB_lF1d9OSw/profile-displayphoto-shrink_800_800/0/1718971147172?e=1724889600&v=beta&t=RD4RRp_ogwCNex7BkOmy0oO68NkL5ParvKJh8y1_05s" alt="Profile Picture">
            </div>
            <a href="https://www.youtube.com/playlist?list=PLs-PsDpuAuTeNx3OgGQ1QrpNBo-XE6VBh" class="button docker-button">Docker - Basics to Brilliance</a>
            <a href="https://www.linkedin.com/in/kastro-kiran/" class="button linkedin-button">LinkedIn Connect</a>
        </div>
    </body>
    </html>
    '''
    return render_template_string(html_content)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)