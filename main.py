from flask import Flask, request, render_template, jsonify

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/reverse', methods=['POST'])
def reverse_string():
    try:
        data = request.form.get('input_string', '')
        if not data:
            return jsonify({'error': 'Input string is missing'}), 400
        reversed_string = data[::-1]
        return render_template('result.html', reversed_string=reversed_string)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

