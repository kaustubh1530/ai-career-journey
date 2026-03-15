from flask import Flask, render_template, request, redirect
import pandas as pd
from datetime import datetime

app = Flask(__name__)

EXCEL_FILE = "inventory.xlsx"

# Dashboard
@app.route("/")
def dashboard():
    # Read Excel
    df = pd.read_excel(EXCEL_FILE, sheet_name="Inventory")
    products = df.to_dict(orient="records")
    return render_template("index.html", products=products)

# Add Product
@app.route("/add-product", methods=["GET", "POST"])
def add_product():
    if request.method == "POST":
        product_name = request.form["product_name"]
        category = request.form["category"]
        quantity = int(request.form["quantity"])
        location = request.form["location"]

        # Read existing inventory
        df = pd.read_excel(EXCEL_FILE, sheet_name="Inventory")

        # Generate new ID
        new_id = len(df) + 1

        # Set quantities based on location
        store_qty = quantity if location == "Store" else 0
        warehouse_qty = quantity if location == "Warehouse" else 0

        # New row
        new_row = {
            "ID": new_id,
            "Product Name": product_name,
            "Category": category,
            "Store Qty": store_qty,
            "Warehouse Qty": warehouse_qty,
            "Last Updated": datetime.now()
        }

        # Add new row
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)

        # Save back to Excel
        with pd.ExcelWriter(EXCEL_FILE, engine="openpyxl", mode="a", if_sheet_exists="replace") as writer:
            df.to_excel(writer, sheet_name="Inventory", index=False)

        return redirect("/")

    return render_template("add_product.html")


if __name__ == "__main__":
    app.run(debug=True)