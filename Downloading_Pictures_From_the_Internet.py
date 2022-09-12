from flask import Flask, render_template, request
import urllib.request
import os


app = Flask(__name__)

@app.route('/', methods = ['GET'])
def main():
    return render_template('download_pictures.html')


@app.route('/downloading_image_result', methods = ['GET','POST'])
def downloadingImageResult():
    imageNamesControlTrue = []
    imageNamesControlFalse = []
    if request.method == 'POST':
        images = request.form['images']
        imageNames = request.form['imageNames']
        if len(images.split(',')) == len(imageNames.split(',')):
            imageNamesSplit = imageNames.split(',')
            counter = 0
            for image in images.split(','):
                try:
                    urllib.request.urlretrieve(image,imageNamesSplit[counter])
                    imageNamesControlTrue.append([True,image,imageNamesSplit[counter]])
                except:
                    imageNamesControlFalse.append([False,image,imageNamesSplit[counter]])
                counter += 1

            if len(imageNamesControlTrue) == 0:
                imageNamesControlTrue = 0
            if len(imageNamesControlFalse) == 0:
                imageNamesControlFalse = 0
            
            return render_template('download_pictures_result.html',
            imageNamesControlTrue = imageNamesControlTrue,
            imageNamesControlFalse = imageNamesControlFalse)

        else:
            return "Error"
    
    else:
        return 'For post requests only.'



if __name__ == '__main__':
    app.run(debug=True, port=5000)