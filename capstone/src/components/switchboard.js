import React, { Component } from "react";
import { connect } from "react-redux";

import LinearProgress from "@material-ui/core/LinearProgress";
import Switch from "@material-ui/core/Switch";
import Button from "@material-ui/core/Button";

import { fetchDevices, setDeviceState } from "../actions";

function DeviceItem(props) {

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
          Device: {props.device.name} |
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
