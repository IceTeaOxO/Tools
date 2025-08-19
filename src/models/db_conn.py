# import pymssql
# from app.config import server__, database__, username__, password__


# def get_connection():
#     server = server__
#     database = database__  
#     username = username__
#     password = password__
#     try:
#         connection = pymssql.connect(
#             server=server,
#             database=database,
#             user=username,
#             password=password,
#         )
#         return connection
#     except Exception as e:
#         error_logger.error(f"Error connecting to the database: {e}")
