document.addEventListener("DOMContentLoaded", fetchTasks);

function fetchTasks() {
    fetch('/get-tasks')
    .then(response => response.json())
    .then(tasks => {
        const taskList = document.getElementById("taskList");
        taskList.innerHTML = "";
        tasks.forEach(task => {
            const li = document.createElement("li");
            li.className = task.completed ? "completed" : "";

            const checkbox = document.createElement("input");
            checkbox.type = "checkbox";
            checkbox.className = "checkbox";
            checkbox.checked = task.completed;
            checkbox.onclick = () => toggleTask(task.id);

            const span = document.createElement("span");
            span.textContent = task.task;

            const deleteBtn = document.createElement("button");
            deleteBtn.textContent = "Delete";
            deleteBtn.className = "delete-btn";
            deleteBtn.onclick = () => deleteTask(task.id);

            li.appendChild(checkbox);
            li.appendChild(span);
            li.appendChild(deleteBtn);
            taskList.appendChild(li);
        });
    });
}

function addTask() {
    const taskInput = document.getElementById("taskInput");
    const task = taskInput.value.trim();

    if (task === "") {
        alert("Task cannot be empty!");
        return;
    }

    fetch('/add-task', {
        method: 'POST',
        body: JSON.stringify({ task: task }),
        headers: { 'Content-Type': 'application/json' }
    })
    .then(response => response.json())
    .then(data => {
        fetchTasks();
        taskInput.value = "";
    });
}

function deleteTask(taskId) {
    fetch(`/delete-task/${taskId}`, { method: 'DELETE' })
    .then(response => response.json())
    .then(data => fetchTasks());
}

function toggleTask(taskId) {
    fetch(`/toggle-task/${taskId}`, { method: 'PUT' })
    .then(response => response.json())
    .then(data => fetchTasks());
}
