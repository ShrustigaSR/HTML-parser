from flask import Flask, render_template, request, send_file
from bs4 import BeautifulSoup
from werkzeug.utils import secure_filename
import json
import os

app = Flask(__name__)
app.config['UPLOAD_EXTENSIONS'] = ['.html']
def parse_html(file_path):
    with open(file_path) as f:
        soup = BeautifulSoup(f, 'html.parser')

    output = {
        "capitals": [],
        "summary": {"numberOfCapitals": 0}
    }

    capitals = [x.text.strip() for x in soup.find_all("strong", {"class": "capital"})]
    states = [y.text.strip() for y in soup.find_all("span", {"class": "state"})]

    length = 0 
    for x in capitals:
      if x!="":
         length+=1
    output["summary"]["numberOfCapitals"] = length

    for z in range(len(capitals)):
        output["capitals"].append({"capital": capitals[z], "state": states[z]})

    return output

@app.route('/upload')
def upload_form():
    return render_template('sample.html')

@app.route('/uploader', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        
        f = request.files['file']
        if f.filename == '':
            error_message = "No selected file!"
            return render_template('sample.html', error_message=error_message)

        file_path = secure_filename(f.filename)
        file_ext = os.path.splitext(file_path)[1]
        if file_ext not in app.config["UPLOAD_EXTENSIONS"]:
             error_message = f"Invalid file extension. Allowed extension are: .html"
             return render_template('sample.html', error_message=error_message)
        f.save(file_path)

        parsed_data = parse_html(file_path)
        
        print(parsed_data)

        with open('result.json','w') as y:
            json.dump(parsed_data,y,indent = 4)
        return send_file('result.json', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
