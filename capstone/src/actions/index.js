import API from '../services/api'

/* 
these are set up as below
if there is no arguement passed then there is no need to use payload:
if there is an arguement payload is that variable passed
it can be whatever, in this case it is just nr
*/
export const GET_DEVICES = 'GET_DEVICES'
function receiveDevices(json) {
  console.log(json)
  return {
    type: GET_DEVICES,
    fetching: false,
    devices: json,
  }
}

export const GET_HVAC_SETTINGS = 'GET_HVAC_SETTINGS'
function receiveHVACSettings(json) {
  console.log(json)
  return {
    type: GET_HVAC_SETTINGS,
    fetching: false,
    settings: json[0],
  }
}

export const DEVICE_STATE_CHANGE = 'DEVICE_STATE_CHANGE'
function deviceStateChanged(json) {
  return {
    type: DEVICE_STATE_CHANGE,
    device: json
  }
}

export const SET_HVAC_TEMP = 'SET_HVAC_TEMP'
function receivedHVACSet(json) {
  return {
    type: SET_HVAC_TEMP,
    device: json
  }
}

function requestDevices() {
  return {
    type: GET_DEVICES,
    fetching: true
  }
}

export function setDeviceState(deviceId, isOn) {

  const targetString = isOn ? "ON" : "OFF";

  return function (dispatch) {

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
  return function (dispatch) {

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

export function getHVAC() {
  return function (dispatch) {
    console.log("Getting HVAC")

    return API.get(`device/thermostat`)
      .then(
        response => response.data,

        error => console.log('An error occurred.', error)
      )
      .then(json =>
        dispatch(receiveHVACSettings(json))
      )
  }
}

export function setHVAC(set_f, low_f, high_f) {
  return function (dispatch) {
    console.log("setting HVAC");

    return API.put(`device/thermostat/${set_f}/${high_f}/${low_f}`)
      .then(
        response => response.data,

        error => console.log('An error occurred.', error)
      )
      .then(json =>
        dispatch(receivedHVACSet(json[0]))
      )
  }
}