import React from "react";
import ProjectCard from "./ProjectCard";

const projects = [
  {
    id: 1,
    title: "Micrograd",
    short_description: "A tiny autograd engine",
    image_url: "https://via.placeholder.com/400x300?text=Micrograd"
  },
  {
    id: 2,
    title: "Makemore",
    short_description: "Character-level language model",
    image_url: "https://via.placeholder.com/400x300?text=Makemore"
  }
];

const ProjectGrid = () => {
    return (
        <div className="gap-6 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3">
            {projects.map((project) => (
                <ProjectCard key={project.id} project={project} />
            ))}
        </div>
    )
}

export default ProjectGrid;