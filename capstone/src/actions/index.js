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

/*
houseTemp will display inside temp of house and outsideTemp is outside temp
this may change bc the information may be pulled from the data base
*/
export const houseTemp = () => {
    return {
        type: 'INSIDE'
    };
};

export const outsideTemp = () => {
    return {
        type: 'OUTSIDE'
    };
};