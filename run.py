from flask import Flask,render_template
app=Flask(__name__)
@app.route('/')
def homepage():
    # return "hghjvhbwexe"
    render_template("index.html")
try:
    if __name__ == '__main__':
        app.run(debug=True)
except:
    pass