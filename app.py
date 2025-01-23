from flask import Flask, render_template, request
import pandas as pd
app = Flask(__name__)

# Routes
@app.route('/')
def home():
    return render_template('home.html')
# Route for the products page
@app.route('/products')
def products():
    # Load the Excel file using pandas (change the path to your actual file)
    df = pd.read_excel('products.xlsx')  # Replace with your file path

    # Convert the data to a list of dictionaries (or you can use .to_html() to generate an HTML table)
    products_data = df.to_dict(orient='records')

    # Pass the data to the template
    return render_template('products.html', data=products_data)


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
