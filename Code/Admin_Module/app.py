from flask import Flask, redirect, url_for, request , render_template
import data
app = Flask(__name__, template_folder="templates")
# @app.route('/')
# def success():
#   return render_template('index.html')
@app.route('/', methods=["GET", "POST"])
def login():
    if(request.method == 'POST'):
        tag = request.form['tag']
        pattern = request.form['pattern']
        res = request.form['res']
        value = data.insertData(tag, pattern, res)
        print(value)
        # return redirect(url_for('login'))
        return render_template('admin.html')

    else:
        tag = request.args.get('tag')
        pattern = request.args.get('pattern')
        res = request.form.get('res')
        value = data.insertData(tag, pattern, res)

        print(value)
        # return redirect(url_for('login'))
        return render_template('admin.html')

@app.route('/files', methods=["GET", "POST"])
def files():
    
    if request.method == "POST":
        file = request.files['file']
        data.excelToJson(file)
    return render_template('upload.html')
    # return redirect(url_for('admin'))

if __name__ == "__main__":
    app.run(debug=True)