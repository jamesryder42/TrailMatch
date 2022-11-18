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




const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <div>
    <NavBar />
    <SideBar />
  </div>


      //
      //   <h1>React Router Contacts</h1>
      //   <div>
      //     <form id="search-form" role="search">
      //       <input
      //         id="q"
      //         aria-label="Search contacts"
      //         placeholder="Search"
      //         type="search"
      //         name="q"
      //       />
      //       <div
      //         id="search-spinner"
      //         aria-hidden
      //         hidden={true}
      //       />
      //       <div
      //         className="sr-only"
      //         aria-live="polite"
      //       ></div>
      //     </form>
      //     <form method="post">
      //       <button type="submit">New</button>
      //     </form>
      //   </div>
      //   <nav>
      //     <ul>
      //       <li>
      //         <a href={`contacts/1`}>Your Name</a>
      //       </li>
      //       <li>
      //         <a href={`contacts/2`}>Your Friend</a>
      //       </li>
      //     </ul>
      //   </nav>
);
