from flask import Flask, render_template

app = Flask('__name__')
@app.route('/Meu primeiro template')
def index():
    return render_template('/index.html')

@app.route('/unifran')
def unifran():
    return render_template('/unifran.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')