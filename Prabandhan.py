from flask import Flask,render_template,request

import os
from Predictor import find_potholes
app = Flask(__name__)


@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        if 'file1' not in request.files:
            return 'there is no file1 in form!'
        file1 = request.files['file1']
        filename=file1.filename
        path = os.path.join("./static", filename)
        file1.save(path)
        print(path)
        data=find_potholes(filename)
        print(data)
        return render_template('index.html',filename=filename,potholes=data)
    return render_template('index.html')



if __name__=="__main__":
    app.run(debug=True)
