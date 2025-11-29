from sqlalchemy import Column, Integer, String, JSON
from database import Base


class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    short_description = Column(String)
    detailed_description = Column(String)
    image_url = Column(String)
    tech_stack = Column(JSON)
