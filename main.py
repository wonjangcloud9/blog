from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="view")


@app.get("/")
async def read_item(request: Request):
    return templates.TemplateResponse("main.html", {"request": request})
