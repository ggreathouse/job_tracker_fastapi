from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from config import settings
import models
from database import SessionLocal, engine

app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)

models.Base.metadata.create_all(bind=engine)

#staticfiles() is the sub for the app name which tells the app that this mount is only for staticfiles
app.mount('/static', StaticFiles(directory='static'), name='static')
templates = Jinja2Templates(directory='templates')


@app.get('/', response_class=HTMLResponse)
async def home_page(request: Request):
    
    return templates.TemplateResponse('/pages/home.html', {'request': request})

