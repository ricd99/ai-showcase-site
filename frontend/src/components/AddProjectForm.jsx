import React, { useState } from "react";

const AddProjectForm = ({ addProject }) => {
    const [projectName, setProjectName] = useState("");

    const handleSubmit = (event) => {
        event.preventDefault();
        if (projectName) {
            addProject(projectName);
            setProjectName("");
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <input
            type="text"
            value={projectName}
            onChange={(e) => setProjectName(e.target.value)}
            placeholder="Enter project name"
            />
            <button type="submit">Add Project</button>
        </form>
    );
};

export default AddProjectForm;