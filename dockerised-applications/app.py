from flask import Flask
from prometheus_client import Counter, generate_latest

app = Flask(__name__)
view_metric = Counter('view', 'Product view', ['product'])
buy_metric = Counter('buy', 'Product buy', ['product'])

@app.route('/view/<id>')
def view_product(id):
    view_metric.labels(product=id).inc()
    return "View %s" % id

@app.route('/buy/<id>')
def buy_product(id):
    buy_metric.labels(product=id).inc()
    return "Buy %s" % id

@app.route('/metrics')
def metrics():
    return generate_latest()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
