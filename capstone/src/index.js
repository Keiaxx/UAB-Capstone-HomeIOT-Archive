import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import { createStore } from 'redux';

//
import allReducers from './reducers';
import { Provider } from 'react-redux'; //connects global state (store) to our app

/*the following is react-redux*/
const store = createStore(
    allReducers,
    window.__REDUX_DEVTOOLS_EXTENSION__ && window.__REDUX_DEVTOOLS_EXTENSION__()
    );

//Provider's prop store takes one param, store = {**your allReducers** which is saved in this app as store}
ReactDOM.render(
    <Provider store ={store}> 
        <App/>
    </Provider>,
    document.getElementById('root')
);