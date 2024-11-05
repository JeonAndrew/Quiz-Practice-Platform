import './App.css';
import CoursePage from './pages/CoursePage/CoursePage';
import HomePage from './pages/HomePage/HomePage';
import LoginPage from './pages/LoginPage/LoginPage';

import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";

function App() {
  return (
    <div className="App">
      <Router>
        <nav>
          <ul>
            <li><Link to="/home">Home</Link></li>
            <li><Link to="/login">Login</Link></li>
            <li><Link to="/course">Course</Link></li>
          </ul>
        </nav>
        <Routes>
          <Route path="*" element={<HomePage />} />
          <Route path="/login" element={<LoginPage />} />
          <Route path="/course" element={<CoursePage />} />
        </Routes>
      </Router>
    </div>
  );
}

export default App;
