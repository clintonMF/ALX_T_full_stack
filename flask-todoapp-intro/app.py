from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', data=[
        {'description': 'todo1'},
        {'description':'todo2'},
        {'description':'todo3'}
    ])
    
    
if __name__ == '__main__':
    app.run()