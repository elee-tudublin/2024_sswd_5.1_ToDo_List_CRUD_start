from typing import Annotated
from fastapi import APIRouter, Form
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

# import service functions
from app.services.todo_service import getAllTodos, addTodo

from app.models.todo import ToDo

router = APIRouter()

# set location for templates
templates = Jinja2Templates(directory="app/view_templates")

# handle http get requests for the site root /
# return the todos page
@router.get("/", response_class=HTMLResponse)
async def todos(request: Request):

    # note passing of parameters to the page
    return templates.TemplateResponse("todo/todos.html", {"request": request, "todoList": getAllTodos() })


@router.post("/")
def add_item(request: Request, item: str = Form(...)):

    # get item value from the form POST data
    new_todo = addTodo(item)
    return templates.TemplateResponse("todo/partials/todo_li.html", {"request": request, "todo": new_todo})
