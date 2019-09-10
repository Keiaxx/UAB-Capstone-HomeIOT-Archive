/*
the actions are switch cases and each case does what we want to happen to the state
the state in this case is a counter starting at 0
when declaring a function you need to have state = a base case
the 2nd parameter is called action
if you recall the variable nr in our action folder, that was the payload
*/

const counterReducer = (state = 0, action) =>{
    switch(action.type){
        case 'INCREMENT':
            return state + action.payload;
        case 'DECREMENT':
            return state -1;
        default:
            return state;
    }
}

export default counterReducer; 