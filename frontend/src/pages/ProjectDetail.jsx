import React from "react";
import { useParams } from "react-router-dom";

const ProjectDetail = () => {
  const { id } = useParams();

  return (
    <div className="bg-gray-50 min-h-screen">
      <div className="mx-auto px-4 py-8 max-w-4xl">
        <h1 className="mb-4 font-bold text-3xl">Project Detail</h1>
        <p>This is the detail page for project {id}</p>
      </div>
    </div>
  );
};

export default ProjectDetail;
