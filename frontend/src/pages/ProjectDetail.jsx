import React, { useState, useEffect } from "react";
import { useParams, Link } from "react-router-dom";
import axios from "axios";

const ProjectDetail = () => {
  const { id } = useParams();
  const [project, setProject] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    axios
      .get(`http://localhost:8000/api/projects/${id}`)
      .then((response) => {
        setProject(response.data);
        setLoading(false);
      })
      .catch((error) => {
        console.error("Errpr fetching project:", error);
        setLoading(false);
      });
  }, [id]);

  if (loading) {
    return <div className="py-8 text-center">Loading...</div>;
  }

  if (!project || project.error) {
    return <div className="py-8 text-center">Project not found</div>;
  }

  return (
    <div className="bg-gray-50 min-h-screen">
      <div className="mx-auto px-4 py-8 max-w-4xl">
        <Link
          to="/"
          className="inline-block mb-4 text-blue-600 hover:underline"
        >
          Back to Projects
        </Link>
        <h1 className="mb-4 font-bold text-3xl">{project.title}</h1>
        <img
          src={project.image_url}
          alt={project.title}
          className="mb-6 rounded-lg w-full"
        />
        <p className="mb-4 text-xl">{project.short_description}</p>
        <p className="mb-6 text-gray-700">{project.detailed_description}</p>
        <div>
          <h2 className="mb-2 font-bold text-2xl">Tech Stack</h2>
          <div className="flex gap-2">
            {project.tech_stack?.map((tech, index) => (
              <span key={index} className="bg-blue-100 px-3 py-1 rounded text-blue-800">
                {tech}
              </span>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
};

export default ProjectDetail;
