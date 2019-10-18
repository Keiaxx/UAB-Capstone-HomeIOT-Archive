import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import { createStore, applyMiddleware } from 'redux';
import thunk from 'redux-thunk'

//
import reducer from './reducers/switch';
import { Provider } from 'react-redux'; //connects global state (store) to our app

// Material-UI theme
import CssBaseline from '@material-ui/core/CssBaseline';
import { ThemeProvider } from '@material-ui/styles';
import theme from './theme';

/*the following is react-redux*/

const initialState = {
  age:21,
  garage1:            ["off", 0, 0],
  garage2:            ["off", 0, 0],
  frontDoor:          ["off", 0, 0],
  backDoor:           ["off", 0, 0],
  oven:               ["off", 200, 500],
  washingMachine:     ["off", 0, 0],
  devices: {
      fetching: false,
      list: []
  },
};

const store = createStore(
  reducer,
  initialState,
  applyMiddleware(
    thunk
  )
  );

//Provider's prop store takes one param, store = {**your allReducers** which is saved in this app as store}
ReactDOM.render(
  <ThemeProvider theme={theme}>
    <Provider store={store}>
      <CssBaseline />
      <App/>
    </Provider>
  </ThemeProvider>,
    document.getElementById('root')
);