from database import connect_db

def add_customer():
    name = input("ชื่อลูกค้า :")
    phone = input("เบอร์โทรศัพท์ :")

    conn = connect_db()
    c = conn.cursor()
    c.execute("INSERT INTO customers (name, phone) VALUES (?, ?)", (name, phone))
    conn.commit()
    conn.close()

    print("เพิ่มข้อมูลลูกค้าเรียบร้อยแล้ว ✅\n")

def show_customers():
    conn = connect_db()
    c = conn.cursor()
    c.execute("SELECT * FROM customers")
    rows = c.fetchall()

    if not rows:
        print("❌ ยังไม่มีลูกค้าที่บันทึกไว้\n")

    else:
        print("\n 📒 รายชื่อลูกค้า:")
        print("-"*30)
        for row in rows:
            print(f"ID: {row[0]} / ชื่อ: {row[1]} / โทร: {row[2]}")
        print("-"*30 + "\n")
  
    conn.close()
    print()