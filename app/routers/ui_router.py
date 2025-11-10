from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
def home(request: Request):
    # The page itself will fetch the tasks via JS from /tasks/
    return templates.TemplateResponse("index.html", {"request": request})
