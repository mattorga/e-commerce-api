from sqlalchemy import MetaData, Table, Column, Integer, String, Float, DateTime, ForeignKey, Boolean
from sqlalchemy.sql import func

metadata = MetaData()

products_core = Table(
    "products_core",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(255), nullable=False),
    Column("price", Float, nullable=False),
    Column("manufacturer", String, nullable=False),
    Column("category", String, nullable=False),
    Column("stock_quantity", Integer, default=0)
)

products_cpu = Table(
    "products_cpu",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("product_id", Integer, ForeignKey("products_core.id")),
    Column("core_count", Integer, default=1, nullable=False),
    Column("clock_speed", Float, nullable=False),
    Column("socket_type", String, nullable=False),
    Column("tdp", Float, nullable=False), # Thermal Design Power in Watts
)

products_gpu = Table(
    "products_gpu",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("product_id", Integer, ForeignKey("products_core.id")),
    Column("memory", Integer, nullable=False),
    Column("clock_speed", Float, nullable=False),
    Column("boost_clock", Integer, nullable=True)
)

products_motherboard = Table(
    "products_motherboard",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("product_id", Integer, ForeignKey("products_core.id")),
    Column("socket_type", String, nullable=False),
    Column("chipset", String, nullable=False),
    Column("ram_slots", Integer, nullable=False),
    Column("form_factor", String, nullable=True)
)

products_storage = Table(
    "products_storage",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("product_id", Integer, ForeignKey("products_core.id")),
    Column("capacity", Integer, nullable=False),
    Column("interface", String, nullable=False),
    Column("form_factor", String, nullable=False),
    Column("read_speed", Integer, nullable=True), # SSDs
    Column("write_speed", Integer, nullable=True), # SSDs
    Column("rpm", Integer, nullable=True), # HDDs
    Column("cache_size", Integer, nullable=True),
)

products_power = Table(
    "products_power",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("product_id", Integer, ForeignKey("products_core.id")),
    Column("wattage", Integer, nullable=False),
    Column("efficiency_rating", String),
    Column("modular_type", String),
    Column("form_factor", String, nullable=False),
    Column("pcie_connectors", Integer),
    Column("sata_connectors", Integer),
)


users_core = Table(
    "users_core",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String(50), unique=True, nullable=False),
    Column("email", String(100), unique=True, nullable=False),
    Column("hashed_password", String(255), nullable=False),
    Column("first_name", String(50), nullable=True),
    Column("last_name", String(50), nullable=True),
    Column("registration_date", DateTime(timezone=True), server_default=func.now()),
    Column("phone_number", String(9), nullable=True),
    Column("is_superuser", Boolean, nullable=False),
)

users_shipping = Table(
    "users_shipping",
    metadata,
    Column("id", Integer, ForeignKey("users_core.id"), primary_key=True),
    Column("street", String),
    Column("city", String),
    Column("state", String(5)),
    Column("zipcode", String),
)

users_billing = Table(
    "users_billing",
    metadata,
    Column("id", Integer, ForeignKey("users_core.id"), primary_key=True),
    Column("street", String),
    Column("city", String),
    Column("state", String(5)),
    Column("zipcode", String),
)

orders_core = Table(
    "orders_core",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("user_id", Integer, ForeignKey("users_core.id"), nullable=False),
    Column("order_date", DateTime(timezone=True), server_default=func.now()),
    Column("total_amount", Float, nullable=False),
    Column("order_status", String, default="pending"),
    Column("shipping_address_id", Integer, ForeignKey("users_shipping.id")),
    Column("billing_address_id", Integer, ForeignKey("users_billing.id")),
)

order_items = Table(
    "order_items",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("order_id", Integer, ForeignKey("orders_core.id"), nullable=False),
    Column("product_id", Integer, ForeignKey("products_core.id"), nullable=False),
    Column("quantity", Integer, nullable=False),
    Column("price", Float, nullable=False),
)

order_payment = Table(
    "order_payment",
    metadata,
    Column("id", Integer, ForeignKey("orders_core.id"), primary_key=True, nullable=False),
    Column("transaction_id", String, nullable=False),
    Column("payment_method", String, nullable=False),
)