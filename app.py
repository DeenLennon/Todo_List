from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder="templates")

todos = [{"task":"", "done":False}]

@app.route("/")
def home():
    return render_template("index.html", todos = todos)

@app.route("/add", methods=["POST"])
def add():
    todo = request.form['todo']
    todos.append({"task":todo, "done":False})
    return redirect(url_for("home"))

@app.route("/edit/<int:index>", methods=["GET", "POST"])
def edit(index):
    todo = todos[index]
    if request.method == "POST":
        todo["task"] = request.form["todo"]
        return redirect(url_for("home"))
    else:
        return render_template("edit.html", todo=todo, index=index)
    
@app.route("/check/<int:home>")
def check(home):
    todos[home]['done'] = not todos[home]['done']
    return redirect(url_for("home"))

@app.route("/delete/<int:home>")
def delete(home):
    del todos[home]
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)