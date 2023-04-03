from flask import Flask, request, render_template, redirect, url_for
from flask_caching import Cache
import os

app = Flask(__name__)
cache = Cache(app, config={'CACHE_TYPE': 'redis', 'CACHE_REDIS_URL': 'redis://localhost:6379/0'})

# for displaying all images in our folder 

@app.route("/")
@cache.cached(timeout=60)
def indexfun():
    allimages = []
    
    for fileName in os.listdir(r'static'):
        allimages.append(os.path.join(fileName))
    
    return render_template("index.html",imageList=allimages)


# for saving all our uploads 

app.static_folder = 'static'

@app.route('/upload', methods=['POST'])
@cache.cached(timeout=60)
def upload():
    file = request.files['file']
    filename = file.filename
    file.save(os.path.join(app.static_folder, filename))
    return redirect(url_for('indexfun'))

# for deleting an image
@app.route('/delete-file',methods=['DELETE'])
@cache.cached(timeout=60)
def delete():
    fileName = request.args.get('fileName')
    filePath = os.path.join(app.static_folder, fileName)
    os.remove(filePath)
    return 'deleted sucessfully'

if __name__ == '__main__':
    app.run(debug=True)
