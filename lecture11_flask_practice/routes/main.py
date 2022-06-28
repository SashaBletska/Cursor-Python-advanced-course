from app import app
from helpers.file import get_users, write_users
from flask import render_template, request, redirect, Response, url_for


@app.route("/")
def search():
    search_user = request.args.get("search_user")
    users = get_users()
    searched_users = []
    if search_user:
        for user in users:
            s_u = str(search_user)
            u_e = str(user["email"])
            u_f = str(user["first_name"])
            u_l = str(user["last_name"])
            u_w = str(user["work_area"])
            if s_u.lower() == u_e.lower() \
                    or s_u.lower() == u_f.lower() \
                    or s_u.lower() == u_l.lower() \
                    or s_u.lower() == u_w.lower():
                searched_users.append(user)
        if len(searched_users) > 0:
            return render_template("search.html", users=searched_users)
        else:
            return render_template("no-user.html")
    else:
        users = get_users()
        return render_template("index.html", users=users)


@app.route("/user-add")
def user_add():
    return render_template("user-add.html")


@app.route("/users", methods=["POST"])
def save_user():
    users = get_users()
    id = 1
    if len(users) > 0:
        id = len(users) + 1
    user = {
        "id": id,
        "email": request.form.get("email"),
        "first_name": request.form.get("first_name"),
        "last_name": request.form.get("last_name"),
        "work_area": request.form.get("work_area")
    }
    users.append(user)
    write_users(users)
    return redirect("/")


@app.route("/user-edit/<int:id>")
def edit(id):
    users = get_users()
    for user in users:
        if user["id"] == id:
            return render_template("user-add.html", user=user)
    return redirect("/")


@app.route("/users/<int:id>", methods=["POST"])
def update(id):
    users = get_users()
    for user in users:
        if user["id"] == id:
            user["email"] = request.form.get("email")
            user["first_name"] = request.form.get("first_name")
            user["last_name"] = request.form.get("last_name")
            user["work_area"] = request.form.get("work_area")
    write_users(users)
    return redirect("/")


@app.route("/users/delete/<int:id>")
def delete(id):
    users = get_users()
    users_new = []
    id_new = 0
    for user in users:
        if user["id"] != id:
            id_new += 1
            user_new = {
                "id": id_new,
                "email": user["email"],
                "first_name": user["first_name"],
                "last_name": user["last_name"],
                "work_area": user["work_area"]
            }
            users_new.append(user_new)
    users = users_new
    write_users(users)
    return redirect("/")
