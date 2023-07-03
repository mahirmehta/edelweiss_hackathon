from flask import Flask, render_template
from data_processing import process_data
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    # Process the data and create the DataFrame
    data_list = process_data()
    df = pd.DataFrame(data_list)

    # Pass the DataFrame to the template
    return render_template('index.html', data=df.to_html())

if __name__ == '__main__':
    app.run()
