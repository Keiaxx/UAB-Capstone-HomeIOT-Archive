import {
    DEVICE_STATE_CHANGE,
    GET_DEVICES,
    GET_HVAC_SETTINGS,
    SET_HVAC_TEMP
} from '../actions'

const reducer = (state, action) => {
    const newState = { ...state };

    switch (action.type) {
        case GET_HVAC_SETTINGS:
            return {
                ...state,
                hvac: action.settings
            }
        case GET_DEVICES:

            if (action.devices) state.devices.list = action.devices

            let devicesWithStateMappedToBoolean = state.devices.list.map((el) => {
                if (el.state === "ON") {
                    el.state = true
                } else {
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
        /* HERE ************** */
        case SET_HVAC_TEMP:
            return {
                ...state,
                hvac: action.device
            }

        default:
            return newState;
    }

};

export default reducer; 