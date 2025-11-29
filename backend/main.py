import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI()


origins = [
    "http://localhost:5173"  # endpoint (url) of frontend server
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

projects = [
    {
        "id": 1,
        "title": "Micrograd",
        "short_description": "A tiny autograd engine",
        "detailed_description": "Full implementation of backpropagation...",
        "image_url": "https://via.placeholder.com/400x300?text=Micrograd",
        "tech_stack": ["Python", "NumPy"],
    },
    {
        "id": 2,
        "title": "Makemore",
        "short_description": "Character-level language model",
        "detailed_description": "Building language models from scratch...",
        "image_url": "https://via.placeholder.com/400x300?text=Makemore",
        "tech_stack": ["Python", "PyTorch"],
    },
]


@app.get("/")
def root():
    return {"message": "AI Projects API"}


@app.get("/api/projects")
def get_projects():
    return projects


@app.get("/api/projects/{project_id}")
def add_project(project_id: int):
    project = next((p for p in projects if p["id"] == project_id), None)
    if project:
        return project
    return {"error": "Project not found"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
