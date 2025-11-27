import React, { useEffect, useState } from "react";
import api from "../api.js";
import AddProjectForm from "./AddProjectForm.jsx";

const ProjectList = () => {
    const [projects, setProjects] = useState([])

    const fetchProjects = async () => {
        try {
            const response = await api.get("/projects") // api here uses axios configurartion defined in api.js
            setProjects(response.data.projects);    
        } catch (error) {
            console.error("Error fetching projects", error);
        }
    };

    const addProject = async(projectName) => {
        try {
            await api.post("/projects", {name: projectName});
            fetchProjects(); // referseh list after adding project
        }   catch (error) {
            console.error("Error adding project", error);
        }
    };

    useEffect(() => {
        fetchProjects();
    }, []);

    return (
        <div>
            <h2>Project List</h2>
            <ul>
                {projects.map((project, index) => (
                    <li key={index}>{project.name}</li>
                ))}
            </ul>
            <AddProjectForm addProject={addProject} />
        </div>
    );
};

export default ProjectList;