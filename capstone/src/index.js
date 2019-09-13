import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import { createStore } from 'redux';

//
import allReducers from './reducers';
import { Provider } from 'react-redux'; //connects global state (store) to our app

// Material-UI theme
import CssBaseline from '@material-ui/core/CssBaseline';
import { ThemeProvider } from '@material-ui/styles';
import theme from './theme';

/*the following is react-redux*/
const store = createStore(
    allReducers,
    window.__REDUX_DEVTOOLS_EXTENSION__ && window.__REDUX_DEVTOOLS_EXTENSION__()
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