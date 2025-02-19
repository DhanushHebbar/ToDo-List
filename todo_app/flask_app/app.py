"""
from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)

TASKS_FILE = "tasks.json"

# Load tasks from file
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get-tasks', methods=['GET'])
def get_tasks():
    tasks = load_tasks()
    return jsonify(tasks)

@app.route('/add-task', methods=['POST'])
def add_task():
    tasks = load_tasks()
    data = request.json
    task_text = data.get("task")

    if task_text:
        tasks.append({"id": len(tasks) + 1, "task": task_text, "completed": False})
        save_tasks(tasks)
        return jsonify({"message": "Task added!", "tasks": tasks})
    
    return jsonify({"error": "Task cannot be empty"}), 400

@app.route('/delete-task/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    tasks = load_tasks()
    tasks = [task for task in tasks if task["id"] != task_id]
    save_tasks(tasks)
    return jsonify({"message": "Task deleted!", "tasks": tasks})

@app.route('/toggle-task/<int:task_id>', methods=['PUT'])
def toggle_task(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = not task["completed"]
            break
    save_tasks(tasks)
    return jsonify({"message": "Task updated!", "tasks": tasks})

if __name__ == '__main__':
    app.run(debug=True)
"""


#new code

from flask import Flask, render_template, request, jsonify
from flask_cors import CORS  # Allow cross-origin requests
import json
import os

app = Flask(__name__)
CORS(app)  # Enable CORS

TASKS_FILE = "tasks.json"

# Load tasks from file
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get-tasks', methods=['GET'])
def get_tasks():
    return jsonify(load_tasks())

@app.route('/add-task', methods=['POST'])
def add_task():
    tasks = load_tasks()
    data = request.json
    task_text = data.get("task")

    if task_text:
        tasks.append({"id": len(tasks) + 1, "task": task_text, "completed": False})
        save_tasks(tasks)
        return jsonify({"message": "Task added!", "tasks": tasks})
    
    return jsonify({"error": "Task cannot be empty"}), 400

@app.route('/delete-task/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    tasks = load_tasks()
    tasks = [task for task in tasks if task["id"] != task_id]
    save_tasks(tasks)
    return jsonify({"message": "Task deleted!", "tasks": tasks})

@app.route('/toggle-task/<int:task_id>', methods=['PUT'])
def toggle_task(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = not task["completed"]
            break
    save_tasks(tasks)
    return jsonify({"message": "Task updated!", "tasks": tasks})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Allow external access
