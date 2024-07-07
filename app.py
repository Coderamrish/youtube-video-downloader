from flask import Flask, render_template, request, send_file
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        # YouTube download logic here...
        # For now, we'll just simulate a success
        success = True
        title = "Example Video"
        filename = "example.mp4"
        if success:
            return render_template('index.html', success=success, title=title, filename=filename)
        else:
            return render_template('index.html', error="Download failed")
    return render_template('index.html')

@app.route('/download/<filename>')
def download_file(filename):
    return send_file(os.path.join('downloads', filename))

if __name__ == "__main__":
    app.run(debug=True)