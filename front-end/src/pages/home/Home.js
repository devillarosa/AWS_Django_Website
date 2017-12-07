import React, { Component } from 'react';
import './Home.css';

import { Link, Route, Switch } from 'react-router-dom'

class Home extends Component {
  render() {
    return (
      <div className="Home">
        <div className="jumbotron">
          <div className="container">
            <h1>Welcome to Django Fitness</h1>
            <h2>Getting started is easy</h2>
          </div>
        </div>
        <div className="container">
          <div className="row">
            <div className="col-md-2 add-exercise">
              <h2><Link to="/exercise">Add Exercises</Link></h2>
              <p>Add exercises to your workout regiment</p>
            </div>
            <div className="col-md-2 arrow">
              <h1>&rarr;</h1>
            </div>
            <div className="col-md-2 log-workout">
              <h2><Link to="/workout">Log Workout</Link></h2>
              <p>Record how each exercise went.</p>
            </div>
            <div className="col-md-2 arrow">
              <h1>&rarr;</h1>
            </div>
            <div className="col-md-2 view-history">
              <h2><Link to="/history">View Your History</Link></h2>
              <p>View the history of your workouts</p>
            </div>
          </div>
        </div>
      </div>
    );
  }
}

export default Home;

