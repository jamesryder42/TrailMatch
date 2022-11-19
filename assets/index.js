import React from 'react';
import ReactDOM from 'react-dom/client';

// come back to this: https://stackoverflow.com/questions/29913387/show-hide-components-in-reactjs
class ShowHide extends React.Component {
  constructor() {
    super();
    this.state = {
      childVisibile: false
    }
  }
}

class NavBar extends React.Component {
  render() {
    return (
      <div className="navbar">
        <a href="" className="navbar-brand">TrailMatch</a>
        <a href="about" className="navbar-item">About</a>
        <a href="contact" className="navbar-item">Contact</a>
      </div>
    )
  }
}

class SideBar extends React.Component {
  render() {
    return (
      <div className="sidebar">
          <h1>Saved</h1>
          <ul className="sidebar-items">
            <li>
              <span>Trails</span>
            </li>
            <li>
              <span>Notes</span>
            </li>
            <li>
              <span>Users</span>
            </li>
          </ul>
      </div>
    )
  }
}

// ROOT -----------------------------------------------------------------------

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <div>
    <NavBar />
    <SideBar />
  </div>
);
