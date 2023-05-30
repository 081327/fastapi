#如何设置静态路由和动态路由，包括多级动态路由、路由参数以及静态路由和动态路由的优先级等内容
from fastapi import FastAPI

app = FastAPI()


#根路由
@app.get("/")
def index():
    
    return '<h1>root</h1>'

#静态路由
@app.get("/greet")
def greet():
    
    return '<h1>Hello everyone</h1>'

#静态路由
@app.get("/greet/lining1")
def greetLining():
    
    return '<h1>Hello lining</h1>'


#动态路由
@app.get("/greet/<name>")
def greetName(name):
    
    return '<h1>Hello my {}</h1>'.format(name)

#动态路由
@app.get("/greet/<a1>/<a2>/<a3>")
def args1(a1,a2,a3):
    
    return '<h1>{},{},{}</h1>'.format(a1,a2,a3)

#动态路由
@app.get("/greet/<a1>-<a2>-<a3>")
def args2(a1,a2,a3):
    
    return '<h1>{}*{}*{}</h1>'.format(a1,a2,a3)



#运行
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)