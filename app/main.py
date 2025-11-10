# from fastapi import FastAPI
# from app.routers.task_router import router as task_router


# app = FastAPI(title="To-Do List API (In-Memory)")

# # include routes
# app.include_router(task_router, prefix="/tasks", tags=["Tasks"])

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from app.routers.task_router import router as task_router
from app.routers.ui_router import router as ui_router

app = FastAPI(title="To-Do List API (In-Memory)")

# If your HTML is served from the same app, CORS is optional.
# If you also open the HTML from file:// or another port, keep these origins.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for quick demos; tighten for prod
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Static files (CSS, JS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# API routes
app.include_router(task_router, prefix="/tasks", tags=["Tasks"])

# UI routes
app.include_router(ui_router, tags=["UI"])

