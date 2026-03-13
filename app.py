from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage for todos
todos = []
next_id = 1

@app.route('/')
def index():
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add_todo():
    global next_id
    text = request.form.get('text', '').strip()
    if text:
        todos.append({
            "id": next_id,
            "text": text,
            "completed": False
        })
        next_id += 1
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
