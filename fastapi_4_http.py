#获取http请求数据
#使用request.headers.get()读取http请求头数据
#使用request.args.get()读取get请求中的某个字段的值



from fastapi import FastAPI
from flask import request


app = FastAPI()
@app.get("/")
async def main():
    user_agent=request.headers.get('User-Agent')
    return '<h1>Your browser is %s</h1>' % user_agent
@app.get("/abc")
async def abc():
    value=request.args.get('arg')
    return '<h1>arg=%s</h1>' % value

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)