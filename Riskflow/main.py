from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Datos de ejemplo para los gráficos
@app.route('/api/bar_chart_data')
def bar_chart_data():
    data = {
        "series": [
            {
                "data": [10, 8, 6, 4, 2],
                "name": "Products"
            }
        ],
        "categories": ["Parches", "", "", "Headphones", "Camera"]
    }
    return jsonify(data)

@app.route('/api/area_chart_data')
def area_chart_data():
    data = {
        "series": [
            {
                "name": "Purchase Orders",
                "data": [31, 40, 28, 51, 42, 109, 100]
            },
            {
                "name": "Sales Orders",
                "data": [11, 32, 45, 32, 34, 52, 41]
            }
        ],
        "labels": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul"]
    }
    return jsonify(data)

@app.route('/')
def index():
    return render_template('./ui/index.html')

if __name__ == '__main__':
    app.run(debug=True)
