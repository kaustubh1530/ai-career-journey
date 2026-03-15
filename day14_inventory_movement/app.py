from flask import Flask, render_template, request, redirect
import pandas as pd
from datetime import datetime

app = Flask(__name__)

EXCEL_FILE = "inventory.xlsx"


# Dashboard
@app.route("/")
def dashboard():

    df = pd.read_excel(EXCEL_FILE, sheet_name="Inventory")
    products = df.to_dict(orient="records")

    return render_template("index.html", products=products)


# Add Product
@app.route("/add-product", methods=["GET", "POST"])
def add_product():

    df = pd.read_excel(EXCEL_FILE, sheet_name="Inventory")

    if request.method == "POST":

        product_name = request.form["product_name"]
        category = request.form["category"]
        quantity = int(request.form["quantity"])
        location = request.form["location"]

        new_id = len(df) + 1

        store_qty = quantity if location == "Store" else 0
        warehouse_qty = quantity if location == "Warehouse" else 0

        new_row = {
            "ID": new_id,
            "Product Name": product_name,
            "Category": category,
            "Store Qty": store_qty,
            "Warehouse Qty": warehouse_qty,
            "Last Updated": datetime.now()
        }

        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)

        df.to_excel(EXCEL_FILE, sheet_name="Inventory", index=False)

        return redirect("/")

    return render_template("add_product.html")


# Move Inventory
@app.route("/move-inventory", methods=["GET", "POST"])
def move_inventory():

    df = pd.read_excel(EXCEL_FILE, sheet_name="Inventory")

    if request.method == "POST":

        product_id = int(request.form["product_id"])
        quantity = int(request.form["quantity"])
        move_from = request.form["move_from"]

        index = df.index[df["ID"] == product_id][0]

        if move_from == "Store":
            df.at[index, "Store Qty"] -= quantity
            df.at[index, "Warehouse Qty"] += quantity
        else:
            df.at[index, "Warehouse Qty"] -= quantity
            df.at[index, "Store Qty"] += quantity

        df.at[index, "Last Updated"] = datetime.now()

        df.to_excel(EXCEL_FILE, sheet_name="Inventory", index=False)

        return redirect("/")

    products = df.to_dict(orient="records")

    return render_template("move_inventory.html", products=products)


# Search Inventory
@app.route("/search", methods=["GET", "POST"])
def search():

    result = None

    if request.method == "POST":

        search_term = request.form["product_name"]

        df = pd.read_excel(EXCEL_FILE, sheet_name="Inventory")

        result = df[df["Product Name"].str.contains(search_term, case=False)]

        result = result.to_dict(orient="records")

    return render_template("search.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)