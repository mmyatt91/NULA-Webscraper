from flask import Flask, request, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension
from forms import ResourceMenuForm
from resource_handler import get_resources

app = Flask (__name__)

app.config['SECRET_KEY'] = "4th_try"
debug = DebugToolbarExtension(app)

@app.route("/", methods=[ "GET", "POST"])
def homepage():
    """Show homepage and display Resource dropdown menu"""

    form = ResourceMenuForm()

    if form.validate_on_submit():
        # category_name = form.resource.choices[0]
        category_id = int(form.resource.data)
        # category_name = form.resource.choices[category_id][1]
        return redirect(f"/resources/{category_id}")
        
    else: 
        return render_template("resource_menu.html", form=form)

@app.route("/resources/<int:category_id>", methods=["GET", "POST"])
def show_resources(category_id):
    """Show list resources of category"""

    form = ResourceMenuForm()

    resourceList = get_resources(category_id)
    category_name = form.resource.choices[category_id][1]
    return render_template("resource_list.html", resourceList=resourceList, category_name=category_name)