from flask import Flask,request,render_template
app1=Flask(__name__)

@app1.route('/')
def index():
    return render_template('index.html')  # Make sure the template name matches your file name exactly.

if __name__ == '__main__':
    app1.run(debug=True)




