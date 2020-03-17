from flask import Flask, render_template, url_for, request
import passhash

app = Flask(__name__)




@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')


@app.route('/hash', methods=['GET', 'POST'])
def hash_pass():
    if request.method == 'POST':
        password = request.form['password']
        hashed_pass = passhash.hash_password(password)
        return render_template('index.html', hashed_pass=hashed_pass, password=password, status="default")

@app.route('/dehash' ,methods=['GET', 'POST'])
def verify():
    if request.method == 'POST':
        password = request.form['password2']
        print(password)
        hash = request.form['hash2']
        check = passhash.verify_password(password, hash)
        if check == True:
            return render_template('index.html', status = 'ok', hash =hash, password=password)
        elif check == False:
            return render_template('index.html',status = 'not_ok', hash =hash, password=password)
        elif check == 'default':
            return render_template('index.html',status = 'default', hash =hash, password=password)



if __name__ == "__main__":
    app.run(
        threaded=True,
        host='0.0.0.0',
        debug=True,
        port=5000
    )