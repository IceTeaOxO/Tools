from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import secrets
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.utils import get_openapi
from core.routers import router


# 關閉預設文件
app = FastAPI(
    title="Tools API"
)
app.include_router(router)

# # 設定API文件加密
# security = HTTPBasic()
# def get_current_username(credentials: HTTPBasicCredentials = Depends(security)):
#     correct_username = secrets.compare_digest(credentials.username, docs_username__)
#     correct_password = secrets.compare_digest(credentials.password, docs_password__)
#     if not (correct_username and correct_password):
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Incorrect email or password",
#             headers={"WWW-Authenticate": "Basic"},
#         )
#     return credentials.username

# @app.get("/docs", include_in_schema=False)
# async def get_documentation(username: str = Depends(get_current_username)):
#     return get_swagger_ui_html(openapi_url="/openapi.json", title="docs")


# @app.get("/openapi.json", include_in_schema=False)
# async def openapi(username: str = Depends(get_current_username)):
#     return get_openapi(title = "ICSAPI", version="1.0.0", routes=app.routes)





# # 根據環境設定不同的 origins
# if ENVIRONMENT == "PRD":
#     cors_origins = [
#         "192.168.21.187"
#     ]
#     allow_credentials = True
#     allow_methods=["GET", "POST", "OPTIONS"]
#     allow_headers=["*"]
#     max_age = 600
# elif ENVIRONMENT == "DEV":
#     cors_origins = ["*"]
#     allow_credentials = True
#     allow_methods = ["*"]
#     allow_headers=["*"]
#     max_age = 600
# else:
#     cors_origins = ["*"]
#     allow_credentials = True
#     allow_methods = ["*"]
#     allow_headers=["*"]
#     max_age = 600



# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )



    
    
    
    
