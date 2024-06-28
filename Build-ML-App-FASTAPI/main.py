from fastapi import FastAPI

#app=FastAPI()
app=FastAPI()

# @my_first_api.get("/")
# async def root():
#     return {"meessage":"Hello world form FASTAPI"}

# @app.get("/") #PAth operation decorator
# async def root():
#     return {"meessage":"Hello world form FASTAPI"}

@app.get("/demo") #PAth operation decorator
async def demo_fun():
    return {"meessage":"Thi is poutput from demo function FASTAPI"}



# path
# POST, PUT, DELETE and GET can be used.

#@app.post()
#@app.put()