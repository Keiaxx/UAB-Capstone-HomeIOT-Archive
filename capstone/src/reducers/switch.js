import {
    DEVICE_STATE_CHANGE,
    GET_DEVICES,
    GET_HVAC_SETTINGS,
    SET_HVAC_TEMP,
    TIME_INTERVAL_CHANGE
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

            console.log(mutatedDevice)

            if (mutatedDevice.geninfo) {
                return {
                    ...state,
                    devices: {
                        fetching: false,
                        list: state.devices.list.map(device =>
                            device.deviceId === mutatedDevice.deviceId ? { ...device, state: newDeviceState } : device
                        )
                    },
                    notification: {
                        visible: true,
                        message: "Device turned on and will use " + Math.round(mutatedDevice.geninfo.usage * 100) / 100 + " kWh"
                    }
                }
            } else {
                return {
                    ...state,
                    devices: {
                        fetching: false,
                        list: state.devices.list.map(device =>
                            device.deviceId === mutatedDevice.deviceId ? { ...device, state: newDeviceState } : device
                        )
                    }
                }
            }
        case "CLOSE_NOTIFICATION":
            return {
                ...state,
                notification: {
                    visible: false,
                    message: ""
                }
            }
        case TIME_INTERVAL_CHANGE:
            let value = action.value
            let unit = action.unit
            return {
                ...state,
                timeinterval: {
                    value: value,
                    unit: unit
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