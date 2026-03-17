from flask import Flask, render_template, request, redirect
import pandas as pd
from datetime import datetime

app = Flask(__name__)

EXCEL_FILE = "inventory.xlsx"


# DASHBOARD
@app.route("/")
def home():

    df = pd.read_excel(EXCEL_FILE, sheet_name="Inventory")

    products = df.to_dict(orient="records")

    total_products = len(df)

    total_store = df["Store Qty"].sum()

    total_warehouse = df["Warehouse Qty"].sum()

    # Low stock warning (warehouse < 5)
    low_stock = df[df["Warehouse Qty"] < 5].to_dict(orient="records")

    return render_template(
        "index.html",
        products=products,
        total_products=total_products,
        total_store=total_store,
        total_warehouse=total_warehouse,
        low_stock=low_stock
    )



# ADD PRODUCT
@app.route("/add-product", methods=["GET","POST"])
def add_product():

    if request.method == "POST":

        name = request.form["product_name"]
        category = request.form["category"]
        quantity = int(request.form["quantity"])
        location = request.form["location"]

        df = pd.read_excel(EXCEL_FILE, sheet_name="Inventory")

        new_id = 1 if df.empty else df["ID"].max() + 1

        store_qty = quantity if location == "Store" else 0
        warehouse_qty = quantity if location == "Warehouse" else 0

        new_product = {
            "ID": new_id,
            "Product Name": name,
            "Category": category,
            "Store Qty": store_qty,
            "Warehouse Qty": warehouse_qty,
            "Last Updated": datetime.now()
        }

        df = pd.concat([df, pd.DataFrame([new_product])], ignore_index=True)

        df.to_excel(EXCEL_FILE, sheet_name="Inventory", index=False)

        return redirect("/")

    return render_template("add_product.html")



# MOVE INVENTORY
@app.route("/move-inventory", methods=["GET","POST"])
def move_inventory():

    df = pd.read_excel(EXCEL_FILE, sheet_name="Inventory")

    if request.method == "POST":

        product_id = int(request.form["product_id"])
        quantity = int(request.form["quantity"])
        employee = request.form["employee"]

        index = df.index[df["ID"] == product_id][0]

        if df.at[index,"Warehouse Qty"] < quantity:
            return "Not enough stock in warehouse"

        df.at[index,"Warehouse Qty"] -= quantity
        df.at[index,"Store Qty"] += quantity

        df.at[index,"Last Updated"] = datetime.now()

        df.to_excel(EXCEL_FILE, sheet_name="Inventory", index=False)

        log_activity(
            "MOVE",
            df.at[index,"Product Name"],
            quantity,
            "Warehouse",
            "Store",
            employee
        )

        return redirect("/")

    products = df.to_dict(orient="records")

    return render_template("move_inventory.html", products=products)



# SEARCH PRODUCT
@app.route("/search", methods=["GET","POST"])
def search():

    results = None

    if request.method == "POST":

        name = request.form["product_name"]

        df = pd.read_excel(EXCEL_FILE, sheet_name="Inventory")

        results = df[df["Product Name"].str.contains(name, case=False)]

        results = results.to_dict(orient="records")

    return render_template("search.html", results=results)



# ACTIVITY LOG
@app.route("/activity")
def activity():

    try:
        df = pd.read_excel(EXCEL_FILE, sheet_name="ActivityLog")
        logs = df.to_dict(orient="records")
    except:
        logs = []

    return render_template("activity_log.html", logs=logs)



# INVENTORY CHECK
@app.route("/inventory-check", methods=["GET","POST"])
def inventory_check():

    df = pd.read_excel(EXCEL_FILE, sheet_name="Inventory")

    products = df.to_dict(orient="records")

    result = None

    if request.method == "POST":

        product_id = int(request.form["product_id"])
        actual = int(request.form["actual_qty"])

        index = df.index[df["ID"] == product_id][0]

        expected = df.at[index,"Store Qty"] + df.at[index,"Warehouse Qty"]

        difference = actual - expected

        result = {
            "expected": expected,
            "actual": actual,
            "difference": difference
        }

    return render_template(
        "inventory_check.html",
        products=products,
        result=result
    )



# LOG ACTIVITY
def log_activity(action, product, quantity, from_loc, to_loc, employee):

    try:
        log_df = pd.read_excel(EXCEL_FILE, sheet_name="ActivityLog")
    except:
        log_df = pd.DataFrame(columns=[
            "Time","Action","Product","Quantity","From","To","Moved By"
        ])

    new_log = {
        "Time": datetime.now(),
        "Action": action,
        "Product": product,
        "Quantity": quantity,
        "From": from_loc,
        "To": to_loc,
        "Moved By": employee
    }

    log_df = pd.concat([log_df, pd.DataFrame([new_log])], ignore_index=True)

    inventory_df = pd.read_excel(EXCEL_FILE, sheet_name="Inventory")

    with pd.ExcelWriter(EXCEL_FILE, engine="openpyxl", mode="w") as writer:

        inventory_df.to_excel(writer, sheet_name="Inventory", index=False)

        log_df.to_excel(writer, sheet_name="ActivityLog", index=False)



if __name__ == "__main__":
    app.run(debug=True)