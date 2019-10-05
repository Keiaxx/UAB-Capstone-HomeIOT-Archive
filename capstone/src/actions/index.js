/* 
these are set up as below
if there is no arguement passed then there is no need to use payload:
if there is an arguement payload is that variable passed
it can be whatever, in this case it is just nr
*/ 

export const increment = (nr) => {
    return {
        type: 'INCREMENT',
        payload: nr
    };
};

export const decrement = () => {
    return {
        type: 'DECREMENT'
    };
};

export const turn = (name, check) => {
    if(check == 0){
        return {
            type: 'TURNON',
            payload: name
        };
    }
    else{
        return {
            type: 'TURNOFF',
            payload: name
        };
    }
};
