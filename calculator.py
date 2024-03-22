from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate_water():
    if request.method == 'POST':
        area = float(request.form['area'])
        weather = request.form['weather']
        
        # Simple logic based on weather conditions
        if weather == 'sunny':
            water_amount = area * 0.8  # More water for sunny conditions
        elif weather == 'cloudy':
            water_amount = area * 0.5
        else:  # rainy
            water_amount = area * 0.3  # Less water for rainy conditions
        
        return render_template('result.html', water_amount=water_amount)

if __name__ == '__main__':
    app.run(debug=True)
