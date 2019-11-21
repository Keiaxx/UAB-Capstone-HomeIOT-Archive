import {
    DEVICE_STATE_CHANGE,
    GET_DEVICES
} from '../actions'

const reducer = (state, action) =>{
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
        case GET_DEVICES:

            if(action.devices) state.devices.list = action.devices

            let devicesWithStateMappedToBoolean = state.devices.list.map((el) => {
                if(el.state === "ON"){
                    el.state = true
                }else{
                    el.state = false
                }
                return el
            })

            return {
                ...state,
                devices: {
                    fetching: action.fetching,
                    list: devicesWithStateMappedToBoolean
                }
            }
        case DEVICE_STATE_CHANGE:
                let mutatedDevice = action.device
                let currDevices = state.devices

                let newDeviceState = mutatedDevice.state === "ON" ? true : false;

                return {
                    ...state,
                    devices: {
                        fetching: false,
                        list: state.devices.list.map(device =>
                            device.deviceId === mutatedDevice.deviceId ? { ...device, state: newDeviceState } : device
                        )
                    }
                }
        default:
            return newState;
    }

};

export default reducer; 
