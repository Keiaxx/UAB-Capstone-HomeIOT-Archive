const changeLights = (state = "nothing", action) =>{
    switch(action.type){
        case "garage1":
            return action;
        case"garage2":
            return action;
        case"waterHeater":
            return action;
        case"win1":
            return action;
        case"win2":
            return action;
        case"win3":
            return action;
        case"washer":
            return action;
        case"dryer":
            return action;
        case"frontD":
            return action;
        case"backD":
            return action;
        case"refridge":
            return action;
        case"stove":
            return action;
        case"HVAC":
            return action;
        case"tv":
            return action;
            default:
            return state;
    }
}

export default changeLights; 