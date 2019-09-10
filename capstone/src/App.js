/* about react-redux */
/* 
React allows constant rendering so if small changes happen to a webpage, the whole page does not need to refresh
React does this through something called a state
a state is an overall object with main variables seen throughout the app itself
managing this state is terrible and a bit confusing so to sort of fix this problem redux was born!!!
redux allows the state to be set up in something called a store and the state is then broken down into actions and reducers
actions hold exported functions that await for a type to be sent to it
then the reducers DO the actions that the actions CALL for
setup for this app is as below:

  src
    actions
      index.js    -> holds exported functions with their types 
    components    -> currently holds nothing
    reducers
      counter.js  -> actions to increase or decreases the counter state
      index.js    -> combines all individual reducers
    App.js        -> where "main" is located, calls components to be rendered 
    index.js      -> holds the store and the allReducers so state can be accessed anywhere in app
*/  

import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';

// Redux
import { Provider, useSelector, useDispatch } from 'react-redux';
import './App.css';

//these are the exported functions that are called from below 
import {increment, decrement} from './actions';

//main
function App() {

  //useSelector(state => state.any reducer that is in your combineReducer function in your reducer folder(located in index.js))
  //useDispatch() allows us to call functions from the actions folders that are in index.js

  const counter = useSelector(state => state.countReducer); 
  const dispatch = useDispatch();                      
  
  //***** keep in mind anything in the return() is rendered, even comments ***** //

  
  //so dispatch is called with the increment() that is in the actions index.js
  //same for decrement()
  return (
    <div className="showcase">
      <h1>Counter {counter}</h1>
      <button onClick={() => dispatch(increment(5))}>+</button>
      <button onClick={() => dispatch(decrement())}>-</button> 
    </div>
  );
}

export default App;
