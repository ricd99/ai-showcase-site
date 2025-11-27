import React from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import ProjectGrid from "./pages/ProjectGrid";
import ProjectDetail from "./pages/ProjectDetail";

const App = () => {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<ProjectGrid />} />
        <Route path="/project/:id" element={<ProjectDetail />} />
      </Routes>
    </BrowserRouter>
  );
};

export default App;