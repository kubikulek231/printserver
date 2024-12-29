from flask import Flask, render_template
from multiprocessing import Process
import time  # Import the time module

app = Flask(__name__, template_folder='template', static_folder='static')

def wait(time_seconds):
    i = 0
    while i < int(time_seconds):
        i += 1
        print("loop running %d" % i)
        time.sleep(1)

@app.route('/')
def index():
    global p
    p = Process(target=wait, args=(2,))
    p.start()
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
