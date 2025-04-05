from database import connect_db

def create_order():
    conn = connect_db()
    c = conn.cursor()

    print("\n📖 รายชื่อลูกค้าที่มีอยู่:")
    c.execute("SELECT * FROM customers")
    customers = c.fetchall()
    for cust in customers:
        print(f"[{cust[0]}]: {cust[1]}")

    customer_id = input("➤ เลือกรหัสลูกค้า:")

    import datetime
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    c.execute("INSERT INTO orders (customer_id, date) Values (?, ?)", (customer_id, today))
    order_id = c.lastrowid

    while True:
        print("\n📦 สินค้าที่มีอยู่:")
        c.execute("SELECT * FROM products")
        products = c.fetchall()
        for p in products:
            print(f"[{p[0]}] {p[1]} - {p[2]} บาท")

        product_id = input("เลือกรหัสสินค้า:")
        quantity = input("จำนวน:")

        c.execute('''
            INSERT INTO order_details (order_id, product_id, quantity)
            VALUES (?, ?, ?)            
        ''', (order_id, product_id, quantity))

        more = input("เพิ่มสินค้าอีกไหม? (y/n): ")
        if more.lower() != 'y':
            break

    conn.commit()
    conn.close()

    print("✅ บันทึกคำสั่งซื้อเรียบร้อยแล้ว\n")

def show_orders():
    conn = connect_db()
    c = conn.cursor()

    c.execute('''
        SELECT orders.id, customers.name, orders.date
        FROM orders
        JOIN customers ON orders.customer_id = customers.id
        ORDER BY orders.id DESC
    ''')
    orders = c.fetchall()

    if not orders:
        print("❌ ยังไม่มีคำสั่งซื้อในระบบ\n")
    else:
        for order in orders:
            order_id, customer_name, date = order
            print(f"\n📄 คำสั่งซื้อ #{order_id} / ลูกค้า: {customer_name} / วันที่: {date}")
            print("-" * 50)

            c.execute('''
                SELECT products.name, order_details.quantity
                FROM order_details
                JOIN products ON order_details.product_id = products.id
                WHERE order_details.order_id = ?
            ''', (order_id,))
            items = c.fetchall()

            for item in items:
                product_name, quantity = item
                print(f"🛒 {product_name} x {quantity}")
            print("-" * 50)
    
    conn.close()
    print()