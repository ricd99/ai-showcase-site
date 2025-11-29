import React from "react";
import ProjectGrid from "../components/ProjectGrid.jsx";

const Home = () => {
  return (
    <div className="bg-gray-50 min-h-screen">
      <header className="bg-blue-600 py-8 text-white">
        <h1 className="font-bold text-4xl text-center">My AI Projects</h1>
      </header>
      <div className="mx-auto px-4 py-8 max-w-6xl">
        <p className="mb-4 text-lg">
          These projects follow the structure of Andrej Karpathy's Zero To Hero
          series.
        </p>
        <p className="mb-4 text-lg">
          Each cell below is one lecture from the series. Within each cell is
          the project from that lecture, as well as side projects I've done
          related to that lecture's topic.
        </p>
      </div>
      <main>
        <div className="px-20">
          <ProjectGrid />
        </div>
      </main>
    </div>
  );
};

export default Home;
