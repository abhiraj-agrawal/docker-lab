from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = '''
<!doctype html>
<html>
<head><title>Simple Calculator</title></head>
<body>
  <center><h2>Enter Two Numbers to Add:</h2>
  <form method="post">
    <label>Number A:</label>
    <input type="number" name="a" step="any" required><br><br>
    <label>Number B:</label>
    <input type="number" name="b" step="any" required><br><br>
    <input type="submit" value="Calculate">
  </form>
  {% if result is not none %}
    <h3>Result: {{ a }} + {{ b }} = {{ result }}</h3>
  {% endif %}</center>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def calculate():
    result = None
    a = b = None
    if request.method == 'POST':
        try:
            a = float(request.form['a'])
            b = float(request.form['b'])
            result = a + b
        except ValueError:
            result = "Invalid input!"
    return render_template_string(HTML_TEMPLATE, result=result, a=a, b=b)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
