from database import connect_db

def add_product():
    name = input("ชื่อสินค้า :")
    price = float(input("ราคาสินค้า :"))

    conn =connect_db()
    c = conn.cursor()

    c.execute("INSERT INTO products (name, price)  VALUES (?, ?)", (name, price))

    conn.commit()
    conn.close()

    print("☑ เพิ่มสินค้าเรียบร้อยแล้ว\n")