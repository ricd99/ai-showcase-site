import uvicorn
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List

from database import SessionLocal, engine, Base
from models import Project

Base.metadata.create_all(bind=engine)

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


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def root():
    return {"message": "AI Projects API"}


@app.get("/api/projects")
def get_projects(db: Session = Depends(get_db)):
    projects = db.query(Project).all()
    return [
        {
            "id": p.id,
            "title": p.title,
            "short_description": p.short_description,
            "detailed_description": p.detailed_description,
            "image_url": p.image_url,
            "tech_stack": p.tech_stack,
        }
        for p in projects
    ]


@app.get("/api/projects/{project_id}")
def add_project(project_id: int, db: Session = Depends(get_db)):
    project = db.query(Project).filter(Project.id == project_id).first()
    if project:
        return {
            "id": project.id,
            "title": project.title,
            "short_description": project.short_description,
            "detailed_description": project.detailed_description,
            "image_url": project.image_url,
            "tech_stack": project.tech_stack,
        }
    raise HTTPException(status_code=404, detail="Project not found")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

# or uvicorn main:app --reload
