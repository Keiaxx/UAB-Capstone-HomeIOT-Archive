const initialState = {
    age:21,
    garage1:            ["off", 0, 0],
    garage2:            ["off", 0, 0],
    frontDoor:          ["off", 0, 0],
    backDoor:           ["off", 0, 0],
    oven:               ["off", 200, 500],
    washingMachine:     ["off", 0, 0]  
};

const reducer = (state = initialState, action) =>{
    const newState = {...state};

    switch(action.type){
        case 'OVEN_ON':
            return {
                ...state,
                oven: ["on", 200, 500]
            }
        case 'OVEN_OFF':
            return {
                ...state,
                oven:["off", 200, 500]
            }
        case 'FRONT_DOOR_ON':
            return {
                ...state,
                frontDoor:["on", 600, 300]
            }
        case 'FRONT_DOOR_OFF':
            return {
                ...state,
                frontDoor:["off", 600, 300]
            }
        default:
            return newState;
    }

};

export default reducer; 