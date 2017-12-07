import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';

import { Link, Route, Switch } from 'react-router-dom'

import  Home from './pages/home/Home';
import Exercise from './pages/exercise/Exercise'; 
import Workout from './pages/workout/Workout'; 
import History from './pages/history/History'; 
import NotFound from './pages/notfound/NotFound'; 

class App extends Component {
  render() {

    return (
      <div className="App">
        <div className="container-fluid">
          <nav className="navbar navbar-inverse">
            <div className="container-fluid">
              <div className="navbar-header">
                <div className="navbar-brand">
                    <Link to="/">Django Fitness</Link>
                </div>
              </div>
              <ul className="nav navbar-nav">
                <li><Link to="/exercise">Exercise</Link></li>
                <li><Link to="/workout">Workouts</Link></li>
                <li><Link to="/history">History</Link></li>
              </ul>
            </div>
          </nav>
          
          <Switch>
            <Route exact path="/" component={Home}/>
            <Route path="/exercise" component={Exercise}/>
            <Route path="/workout" component={Workout}/> 
            <Route path="/history" component={History}/> 
            <Route path="*" component={NotFound}/> 
          </Switch>
          </div>

        </div>
       );
    }
}
export default App;
