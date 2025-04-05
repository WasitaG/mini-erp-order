from database import create_tables
from product import add_product
from customer import add_customer, show_customers
from order import create_order, show_orders

def main_menu():
    while True:
        print(">> เมนูระบบสินค้า <<")
        print("1. เพิ่มสินค้า")
        print("2. เพิ่มลูกค้า")
        print("3. แสดงลูกค้า")
        print("4. สร้างคำสั่งซื้อ")
        print("5. แสดงคำสั่งซื้อ")
        print("6. ออก")

        choice = input("เลือกเมนู (1-6): ")

        if choice == "1":
            add_product()
        elif choice == "2":
            add_customer()
        elif choice == "3":
            show_customers()
        elif choice == "4":
            create_order()
        elif choice == "5":
            show_orders()
        elif choice == "6":
            print("☒ ออกจากระบบ ☒")
            break
        else:
            print("⚠︎ กรุณาเลือกหมายเลข 1 หรือ 6 เท่านั้น\n")

if __name__=="__main__":
    create_tables()
    print("Database and table created successfully. ✔")
    main_menu()