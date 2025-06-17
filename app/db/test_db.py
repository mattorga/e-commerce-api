from sqlalchemy import select, insert, delete, update
from app.db.database import get_engine, create_tables
from app.db.models import products_core, users_core, orders_core, order_items

def setup_database():
    create_tables()

insert_stmt = insert(products_core).values(
            name="Test Product",
            description="A test product",
            price=29.99
        )

multiple_insert_stmt = insert(products_core).values([
        {
            "name": "Gaming Laptop",
            "description": "Laptop for Gaming",
            "price": 1199.99
        },
        {
            "name": "Work Laptop",
            "description": "Laptop for Working",
            "price": 399.99
        },
        {
            "name": "Personal Laptop",
            "description": "Laptop for Personal Matters",
            "price": 599.99
        }
    ])

update_stmt = update(products_core).where(products_core.c.id == 9).values(price=1099.99)

delete_stmt = delete(products_core).where(products_core.c.name == "Test Product")

select_stmt = select(products_core)

# Exercises
filter_stmt = select(products_core).where(products_core.c.price > 500)
update_stmt = update(products_core).values(price=products_core.c.price*0.10 + products_core.c.price)

def test(operation):
    engine = get_engine()

    with engine.connect() as connection:
        connection.execute(operation)
        connection.commit()
        
        result = connection.execute(select_stmt)
        print("Products:")
        for row in result:
            print(row)

if __name__ == "__main__":
    # Run only once
    # setup_database()

    # test(update_stmt)
    pass
    