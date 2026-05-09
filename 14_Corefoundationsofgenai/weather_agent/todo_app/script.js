const addTaskButton = document.getElementById("add-task");

const taskInput = document.getElementById("new-task");

const taskList = document.getElementById("task-list");

addTaskButton.addEventListener("click", function () {

    const taskText = taskInput.value.trim();

    if (taskText === "") {
        return;
    }

    const li = document.createElement("li");

    const span = document.createElement("span");

    span.textContent = taskText;

    const deleteButton = document.createElement("button");

    deleteButton.textContent = "Delete";

    deleteButton.classList.add("delete-btn");

    deleteButton.addEventListener("click", function () {
        li.remove();
    });

    li.appendChild(span);

    li.appendChild(deleteButton);

    taskList.appendChild(li);

    taskInput.value = "";
});