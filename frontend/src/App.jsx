import React from "react";
import "./App.css";
import ProjectList from "./components/Projects.jsx"

const App = () => {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Project Showcase</h1>
      </header>
      <main>
        <ProjectList />
      </main>
    </div>
  )
}

export default App;