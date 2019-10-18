import API from '../services/api'

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
        case "FRONT_DOOR_ON":
            return{
                type:"FRONT_DOOR_ON",
            }
        default:
    }
};

export const GET_DEVICES = 'GET_DEVICES'
function receiveDevices(json) {
    console.log(json)
  return {
    type: GET_DEVICES,
    fetching: false,
    devices: json,
  }
}

export const DEVICE_STATE_CHANGE = 'DEVICE_STATE_CHANGE'
function deviceStateChanged(json){
    return {
        type: DEVICE_STATE_CHANGE,
        device: json
    }
}

function requestDevices() {
  return {
    type: GET_DEVICES,
    fetching: true
  }
}

export function setDeviceState(deviceId, isOn){

    const targetString = isOn ? "ON" : "OFF";

    return function(dispatch) {

        dispatch(requestDevices())
    
        return API.put(`device/${deviceId}/setstate/${targetString}`)
          .then(
            response => response.data,
  
            error => console.log('An error occurred.', error)
          )
          .then(json =>
            dispatch(deviceStateChanged(json))
          )
      }
}

export function fetchDevices() {
    return function(dispatch) {
  
      dispatch(requestDevices())
  
      return API.get(`device`)
        .then(
          response => response.data,

          error => console.log('An error occurred.', error)
        )
        .then(json =>
          dispatch(receiveDevices(json))
        )
    }
}