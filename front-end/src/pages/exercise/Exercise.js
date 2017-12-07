import React, { Component } from 'react';
import './Exercise.css';

class Exercise extends Component {
  render() {
    return (
      <div className="Exercise">
        <div className="container">
          <div className="col-md-4 available-exercise">
            <h1>Exercises</h1>
          </div>
          <div className="col-md-4 arrow">
            <h1>&rarr;</h1>
          </div>
          <div className="col-md-4 user-exercise">
            <h1>Your Exercises</h1>
          </div>
        </div>
      </div>
    );
  }
}

export default Exercise;
