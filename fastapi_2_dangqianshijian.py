#在浏览器中显示当前服务器中的时间
#导入FaskAPI
from fastapi import FastAPI
from time import *
#创建FastAPI对象
app = FastAPI()
#定义路由方法
@app.get("/")
async def hello():
    #返回服务器的时间
    return strftime('%Y-%m-%d %H:%M:%S',localtime(time()))
#运行
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
