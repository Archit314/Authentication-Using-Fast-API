# from sqlmodel import SQLModel, create_engine

# # Replace these values with your actual PostgreSQL credentials


# # PostgreSQL connection string
# connection_string = f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# # No need for connect_args when using PostgreSQL
# engine = create_engine(connection_string, echo=True)

# def init_db():
#     try:
#         # Try to connect and execute a dummy query
#         with engine.connect() as conn:
#             conn.execute("SELECT 1")
#         print("✅ Database connection successful.")
#         SQLModel.metadata.create_all(engine)
#     except OperationalError as e:
#         print("❌ Failed to connect to the database.")
#         print(e)
