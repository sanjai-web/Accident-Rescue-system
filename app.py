from flask import Flask, render_template, request
import ml  # Import the ml.py script

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        location_name = request.form['location']
        if ml.generate_graph(location_name):
            return render_template('index.html', location=location_name, graph=True)
        else:
            return render_template('index.html', error="Location not found!")
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)