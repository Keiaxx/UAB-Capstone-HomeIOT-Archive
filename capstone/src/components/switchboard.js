import React, { Component } from "react";
import { connect } from "react-redux";

import LinearProgress from "@material-ui/core/LinearProgress";
import Switch from "@material-ui/core/Switch";
import Button from "@material-ui/core/Button";

import { fetchDevices, setDeviceState } from "../actions";

function DeviceItem(props) {

    let translation = {
        "microwave": "電子レンジ",
        "refrigerator": "冷蔵庫",
        "stove": "レンジ",
        "oven": "オーブン",
        "dishwasher": "食器洗い機",
        "kitchen_door": "キッチンドア",
        "kitchen_window": "キッチン窓",
        "main_hvac": "メイン",
        "garage_door": "ガレージのドア",
        "water_heater": "湯沸かし器",
        "living_room_tv": "リビングルームテレビ",
        "living_room_light": "リビングルームライト",
        "main_door": "メインドア",
        "livingroom_window": "リビングルーム窓",
        "Bedroom1_light": "ベッドルーム1ライト",
        "bedroom1_tv": "ベッドルーム1ライトテレビ",
        "bedroom1_window": "ベッドルーム1窓",
        "Bedroom2_light": "ベッドルーム2ライト",
        "bedroom2_tv": "ベッドルーム2ライト",
        "bedroom_window": "ベッドルーム2窓",
        "bathroom1_exhaust_fan": "浴室排気1ファン",
        "bathroom1_light": "浴室排気1",
        "bathroom1_bath_water_meter": "浴室排気1",
        "bathroom2_exhaust_fan": "浴室排気2ファン",
        "bathroom2_light": "浴室排気2ライト",
        "bathroom2_shower_water_meter": "浴室排気2水道メーター",
        "washer": "洗濯機",
        "washer_water_meter": "水道メーター",
        "dryer": "ドライヤー",
        "kitchen_light": "キッチンライト"
    }

    let [state, setState] = React.useState({
        checked: props.device.state,
    });

    let handleDeviceStateChange = (dispatch, device) => {
        return event => {
            console.log(
                "Device state mutated for ID: " +
                device.deviceId +
                " setting to " +
                event.target.checked
            );
            let checked = event.target.checked;
            device.state = checked;
            setState({ ...state, checked: checked });
            dispatch(setDeviceState(device.deviceId, checked));
        };
    }


    return (
        <li>
            Device: {props.device.name} / {translation[props.device.name]} |
          <Switch
                checked={state.checked}
                onChange={handleDeviceStateChange(
                    props.dispatch,
                    props.device
                )}
            />
            {props.device.state ? "ON" : "OFF"}
        </li>
    );
}

function DeviceList(props) {
    const dispatch = props.dispatch;
    const rawList = props.devicelist;

    console.log(props.devices);

    const deviceList = rawList.map(device => {
        return (
            <DeviceItem
                dispatch={dispatch}
                device={device}
                key={device.deviceId}
            />
        );
    });

    return <ul>{deviceList}</ul>;
}

class switchBoard extends Component {
    componentDidMount() {
        console.log("Component mounted, loading devices");

        const { dispatch } = this.props;
        dispatch(fetchDevices());
    }

    render() {
        let loadingBar;

        if (this.props.devices.fetching) {
            loadingBar = <LinearProgress />;
        }

        return (
            <div className="swichboard">
                {loadingBar}
                <DeviceList
                    dispatch={this.props.dispatch}
                    devicelist={this.props.devicelist}
                />
            </div>
        );
    }
}

//for every page you need a mapStateToProps for every component
const mapStateToProps = state => {
    return {
        age: state.age,
        oven: state.oven,
        frontDoor: state.frontDoor,
        devices: state.devices,
        devicelist: state.devices.list
    };
};

//
const mapDispatchToProps = dispatch => {
    return {
        TURNED_ON_OVEN: () => dispatch({ type: "OVEN_ON" }),
        TURNED_OFF_OVEN: () => dispatch({ type: "OVEN_OFF" }),
        dispatch: dispatch
    };
};

export default connect(
    mapStateToProps,
    mapDispatchToProps
)(switchBoard);
