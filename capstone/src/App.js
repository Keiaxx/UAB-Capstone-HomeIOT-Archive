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
      index.js    -> combines all individual reducers now in App.js
    App.js        -> where "main" is located, calls components to be rendered 
    index.js      -> holds the store and the allReducers so state can be accessed anywhere in app
*/  

import React, {Fragment} from 'react';
import { BrowserRouter as Router, Route, Switch} from 'react-router-dom';

// Redux
import { useSelector, useDispatch } from 'react-redux'; //connects global state (store) to our app
import './App.css';

//these are the exported functions that are called from below 
import {increment, decrement} from './actions';
import Dashboard from './components/dashboard';
import manualButtons from './components/manuaButtons';


//Material components
import Button from '@material-ui/core/Button';
import Container from '@material-ui/core/Container';
import Typography from '@material-ui/core/Typography';
import Box from '@material-ui/core/Box';
import { makeStyles } from '@material-ui/core/styles';
import AppBar from './components/AppBar';

/*
<Box my={4}>
<div className="showcase">
  <Button variant="contained"  onClick={() => dispatch(increment(5))} color="primary" className={classes.button}>+</Button>
  <Button variant="contained"  onClick={() => dispatch(decrement())} color="primary" className={classes.button}>-</Button>
</div>
</Box>
*/
const useStyles = makeStyles(theme => ({
  button: {
    margin: theme.spacing(1),
  },
  input: {
    display: 'none',
  },
}));

//main
function App() {

  //useSelector(state => state.any reducer that is in your combineReducer function in your reducer folder(located in index.js))
  //useDispatch() allows us to call functions from the actions folders that are in index.js

  const counter = useSelector(state => state.counterReducer);
  const dispatch = useDispatch();                      
  
  //***** keep in mind anything in the return() is rendered, even comments ***** //

  const classes = useStyles();
  //so dispatch is called with the increment() that is in the actions index.js
  //same for decrement()
  return (
      <Container fixed maxWidth='false'>
        <AppBar/>
        <br/>
        <br/>       
        <br/>
        <br/>
        <Router>
        <Fragment>
          <Switch>
            <Route exact path ='/' component={Dashboard} />
            <Route exact path='/manualButtons' component={manualButtons} />
          </Switch>
        </Fragment>
      </Router>

      </Container>
  );
}

export default App;
