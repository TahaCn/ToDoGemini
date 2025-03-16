from fastapi import FastAPI, Request
from starlette.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from .models import Base
from starlette import status
from .database import engine
from .routers.auth import router as auth_router
from .routers.todo import router as todo_router
import os
app = FastAPI()

script_dir = os.path.dirname(__file__)
st_abd_file_path = os.path.join(script_dir, 'static/')

app.mount('static', StaticFiles(directory='static'), name='static')

@app.get("/")
def read_root(request: Request):
    return RedirectResponse(url='/todo/todo-page',status_code=status.HTTP_303_SEE_OTHER)
app.include_router(auth_router)
app.include_router(todo_router)
Base.metadata.create_all(bind=engine)
