import uvicorn

if __name__ == "__main__":
    uvicorn.run("core.main:app", host="0.0.0.0",
                        port=31010, 
                        timeout_keep_alive=15,  # 減少連接保持時間
                        workers=1,  # Windows 建議使用單進程
                        reload=True,
                        )
    
