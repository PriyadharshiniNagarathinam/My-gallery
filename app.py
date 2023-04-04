from flask import Flask, request, render_template, redirect, url_for
import os

app = Flask(__name__)

# for displaying all images in our folder 

@app.route("/")
def indexfun():
    allimages = []
    
    for fileName in os.listdir(r'static'):
        allimages.append(os.path.join(fileName))
    
    return render_template("index.html",imageList=allimages)


# for saving all our uploads 

app.static_folder = 'static'

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    filename = file.filename
    file.save(os.path.join(app.static_folder, filename))
    return redirect(url_for('indexfun'))

# for deleting an image
@app.route('/delete-file',methods=['DELETE'])
def delete():
    fileName = request.args.get('fileName')
    filePath = os.path.join(app.static_folder, fileName)
    os.remove(filePath)
    return 'deleted sucessfully'

if __name__ == '__main__':
    app.run(debug=True)
