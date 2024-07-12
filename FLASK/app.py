from flask import Flask, render_template, request, redirect, url_for

app=Flask(__name__)

#Create wildlife conservation species list
species_list=[
    {"name":"Elephant", "habitant":"Africa"},
    {"name":"Lion", "habitant":"Africa"},
    {"name":"Giraffe", "habitant":"Africa"},
    {"name":"Bat", "habitant":"Africa"},
    {"name":"Penguin", "habitant":"Antarctica"},
    {"name":"Seal", "habitant":"Antarctica"},
    {"name":"Eagle", "habitant":"Antarctica"},
    {"name":"Falcon", "habitant":"Antarctica"},
    {"name":"Ostrich", "habitant":"Antarctica"}
]

@app.route("/")
def index():
    return render_template("index.html", species_list=species_list)

@app.route("/add", methods=["POST", "GET"])
def add_species():
    if request.method == "POST":
        name=request.form["name"]
        habitat=request.form["habitat"]
        species_list.append({"name":name, "habitat":habitat})
        return redirect(url_for("index"))
    return render_template("add_species.html")

if __name__ == "__main__":
    app.run(debug=True)