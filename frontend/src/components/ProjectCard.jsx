import React from "react";
import { Link } from "react-router-dom";

const Projectcard = ({ project }) => {
  return (
    <Link to={`/projects/${project.id}`}>
      <div className="bg-white shadow-md hover:shadow-xl rounded-lg overflow-hidden transition-shadow duration-300 cursor-pointer">
        <img
          src={project.image_url}
          alt={project.title}
          className="w-full h-48 object-cover"
        />
        <div className="p-6">
          <h3 className="mb-2 font-bold text-xl">{project.title}</h3>
          <p className="text-gray-600">{project.short_description}</p>
        </div>
      </div>
    </Link>
  );
};
