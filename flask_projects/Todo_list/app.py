#!/usr/bin/python3

# Importing flask modules 
from flask import Flask, render_template, request, redirect, url_for

# Initializing the Flask application
app = Flask(__name__, template_folder="templates")

# Sample todo list containing a dictionary with a task and its completion status
todos = [{"todo": "Sample Todo", "done": False}]

# Route for the home page
@app.route("/")
def index():
    # Render the index.html template and pass the todos list to it
    return render_template("index.html", todos=todos)

# Route for adding a new todo item, only allows POST requests
@app.route("/add", methods=["POST"])
def add():
    # Get the new todo task from the form data
    todo = request.form["todo"]
    # Add the new task to the todos list with a default 'done' status of False
    todos.append({"task": todo, "done": False})
    # Redirect to the home page to display the updated list
    return redirect(url_for("index"))

# Route for editing an existing todo item, allows GET and POST requests
@app.route("/edit/<int:index>", methods=["GET", "POST"])
def edit(index):
    # Get the todo item to edit based on the index from the URL
    todo = todos[index]
    if request.method == "POST":
        # Update the task if the request method is POST
        todo['task'] = request.form["todo"]
        # Redirect to the home page after updating
        return redirect(url_for("index"))
    else:
        # Render the edit.html template to edit the task, passing the todo item and its index
        return render_template("edit.html", todo=todo, index=index)

# Route for toggling the completion status of a todo item
@app.route("/check/<int:index>")    
def check(index):
    # Toggle the 'done' status of the todo item
    todos[index]['done'] = not todos[index]['done']
    # Redirect to the home page to display the updated status
    return redirect(url_for("index"))

# Route for deleting a todo item
@app.route("/delete/<int:index>")
def delete(index):
    # Remove the todo item from the list based on the index
    del todos[index]
    # Redirect to the home page to display the updated list
    return redirect(url_for("index"))

# Main entry point of the application
if __name__ == "__main__":
    # Run the Flask application in debug mode
    app.run(debug=True)
