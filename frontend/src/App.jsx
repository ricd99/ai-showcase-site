import React from "react";
import "./App.css";
import ProjectList from "./components/Projects.jsx";

const App = () => {
  return (
    <div className="App">
      <div>
        <header className="App-header">
          <h1>My AI Projects</h1>
        </header>
        <p>
          These projects follow the structure of Andrej Karpathy's Zero To Hero
          series.
        </p>
        <p>
          Each cell below is one lecture from the series. Within each cell is
          the project from that lecture, as well as side projeects I've done
          related to that lecture's topic.
        </p>
      </div>
      <main>
        <ProjectList />
      </main>
    </div>
  );
};

export default App;
