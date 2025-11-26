import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List


class Project(BaseModel):
    name: str


class Projects(BaseModel):
    projects: List[Project]


app = FastAPI()

origins = [
    "http://localhost:3000"  # endpoint (url) of frontend server
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

memory_db = {"projects": []}


@app.get("/projects", response_model=Projects)
def get_projects():
    return Projects(projects=memory_db["projects"])


@app.post("/projects", response_model=Project)
def add_project(project: Project):
    memory_db["projects"].append(project)
    return project


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
