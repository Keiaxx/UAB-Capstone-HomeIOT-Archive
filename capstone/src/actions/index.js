/* 
these are set up as below
if there is no arguement passed then there is no need to use payload:
if there is an arguement payload is that variable passed
it can be whatever, in this case it is just nr
*/ 

export const turn = (status) => {
    switch(status){
        case "TURNED_ON_OVEN":
            return{
                type:"OVEN_ON",
            }
        case "TURNED_OFF_OVEN":
            return{
                type:"OVEN_OFF"
            }
            
        case"FRONT_DOOR_ON":
            return{
                type:"FRONT_DOOR_ON",
            }
            
        default:
            
    }
};
