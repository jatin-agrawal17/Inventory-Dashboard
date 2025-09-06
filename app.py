import streamlit as st
import pandas as pd
from db_function import (
    connect_to_db, get_basic_info, get_additonal_tables,
    get_categories, get_suppliers, add_new_mannual_id,
    get_all_products, get_product_history, place_reorder,
    get_pending_reorder, mark_reorder_as_received
)

# ------------------ Sidebar ------------------ #
st.sidebar.title("📦 Inventory Management Dashboard")
options = st.sidebar.radio(
    "📊 Navigation",
    ["📌 Basic Information", "⚙️ Operational Tasks"]
)

# ------------------ Page Title ------------------ #
st.title("📊 Inventory and Supply Chain Dashboard")

# Database connection
db = connect_to_db()
cursor = db.cursor(dictionary=True)

# ------------------ Basic Information ------------------ #
if options == "📌 Basic Information":
    st.header("📊 Basic Metrics")

    basic_info = get_basic_info(cursor)
    keys = list(basic_info.keys())

    # Show metrics in two rows
    col = st.columns(3)
    for i in range(3):
        col[i].metric(label=keys[i], value=basic_info[keys[i]])

    col = st.columns(3)
    for i in range(3, 6):
        col[i-3].metric(label=keys[i], value=basic_info[keys[i]])

    st.markdown("---")

    tables = get_additonal_tables(cursor)
    for labels, data in tables.items():
        with st.expander(f"📑 {labels}"):
            df = pd.DataFrame(data)
            st.dataframe(df, width="stretch")  # ✅ updated

# ------------------ Operational Tasks ------------------ #
elif options == "⚙️ Operational Tasks":
    st.header("⚙️ Operational Tasks")
    selected_task = st.selectbox(
        "Choose a Task",
        ["-- Select --", "➕ Add New Product", "📜 Product History", "📦 Place Reorder", "✅ Receive Reorders"]
    )

    # ------------------ Add Product ------------------ #
    if selected_task == "➕ Add New Product":
        st.subheader("🆕 Add New Product")
        categories = get_categories(cursor)
        suppliers = get_suppliers(cursor)

        with st.form("Add_Product_Form"):
            product_name = st.text_input("Product Name")
            product_category = st.selectbox("Category", categories)
            product_price = st.number_input("Price", min_value=0.0)
            product_stock = st.number_input("Stock", min_value=0, step=1)
            product_level = st.number_input("Reorder Level", min_value=0, step=1)

            suppliers_ids = [s['supplier_id'] for s in suppliers]
            supplier_names = [s['supplier_name'] for s in suppliers]

            supplier_id = st.selectbox(
                "Supplier", options=suppliers_ids,
                format_func=lambda x: supplier_names[suppliers_ids.index(x)]
            )

            submitted = st.form_submit_button("✅ Add Product")

            if submitted:
                if not product_name:
                    st.error("❌ Please enter the product name.")
                else:
                    try:
                        add_new_mannual_id(cursor, db, product_name, product_category,
                                           product_price, product_stock, product_level, supplier_id)
                        st.success(f"🎉 Product {product_name} added successfully")
                    except Exception as e:
                        st.error(f"⚠️ Error in adding the product: {e}")

    # ------------------ Product History ------------------ #
    elif selected_task == "📜 Product History":
        st.subheader("📜 Product Inventory History")
        products = get_all_products(cursor)

        product_names = [p['product_name'] for p in products]
        product_ids = [p['product_id'] for p in products]

        selected_product_name = st.selectbox("Select a Product", options=product_names)

        if selected_product_name:
            selected_product_id = product_ids[product_names.index(selected_product_name)]
            history_data = get_product_history(cursor, selected_product_id)

            if history_data:
                with st.expander("📊 View Full History"):
                    df = pd.DataFrame(history_data)
                    st.dataframe(df, width="stretch")  # ✅ updated
            else:
                st.info("ℹ️ No history found for the selected product.")

    # ------------------ Place Reorder ------------------ #
    elif selected_task == "📦 Place Reorder":
        st.subheader("📦 Place a Reorder")
        products = get_all_products(cursor)

        product_names = [p['product_name'] for p in products]
        product_ids = [p['product_id'] for p in products]

        selected_product_name = st.selectbox("Select a Product", options=product_names)
        reorder_qty = st.number_input("Reorder Quantity", min_value=1, step=1)

        if st.button("📤 Place Reorder"):
            if not selected_product_name:
                st.error("❌ Please select a product.")
            elif reorder_qty <= 0:
                st.error("❌ Reorder quantity must be greater than 0.")
            else:
                selected_product_id = product_ids[product_names.index(selected_product_name)]
                try:
                    place_reorder(cursor, db, selected_product_id, reorder_qty)
                    st.success(f"✅ Order placed for {selected_product_name} with quantity {reorder_qty}")
                except Exception as e:
                    st.error(f"⚠️ Error placing reorder: {e}")

    # ------------------ Receive Reorder ------------------ #
    elif selected_task == "✅ Receive Reorders":
        st.subheader("✅ Mark Reorder as Received")
        pending_reorders = get_pending_reorder(cursor)

        if not pending_reorders:
            st.info("📭 No pending orders to receive.")
        else:
            reorder_ids = [r['reorder_id'] for r in pending_reorders]
            reorder_labels = [f"ID {r['reorder_id']} - {r['product_name']}" for r in pending_reorders]

            selected_label = st.selectbox("Select Reorder to Mark as Received", options=reorder_labels)
            if selected_label:
                selected_reorder_id = reorder_ids[reorder_labels.index(selected_label)]

                if st.button("✅ Mark as Received"):
                    try:
                        mark_reorder_as_received(cursor, db, selected_reorder_id)
                        st.success(f"🎉 Reorder ID {selected_reorder_id} marked as received")
                    except Exception as e:
                        st.error(f"⚠️ Error: {e}")
