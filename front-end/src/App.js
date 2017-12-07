import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';

import { Link, Route, Switch } from 'react-router-dom'

import { BrowserRouter } from 'react-router-dom';
import  Home from './pages/home/Home';
import Exercise from './pages/exercise/Exercise'; 
import Workout from './pages/workout/Workout'; 
import NotFound from './pages/notfound/NotFound'; 

class App extends Component {
  render() {

    return (
      <div>
        <nav className="navbar navbar-light">
          <ul className="nav navbar-nav">
            <li><Link to="/">Home</Link></li>
            <li><Link to="/exercise">Exercise</Link></li>
            <li><Link to="/workout">Workouts</Link></li>
          </ul> 
        </nav>
        <Switch>
          <Route exact path="/" component={Home}/>
          <Route path="/exercise" component={Exercise}/>
          <Route path="/workout" component={Workout}/> 
          <Route path="*" component={NotFound}/> 
        </Switch>

        </div>
       );
    }
}
export default App;
