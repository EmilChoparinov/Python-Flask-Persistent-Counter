from flask import Flask, render_template, session, redirect

server = Flask(__name__)
server.secret_key = "aSecret"

# default route will contain html
@server.route('/')
def index():
    try:
        session['counter'] += 1
    except:
        session['counter'] = 0
    
    return render_template('index.html')

@server.route('/add2', methods=['POST'])
def add2():
    session['counter'] += 1
    return redirect('/')

@server.route('/reset', methods=['POST'])
def reset():
    session['counter'] = 0
    return redirect('/')

server.run(debug=True)