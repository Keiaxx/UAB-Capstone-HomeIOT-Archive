import React, { Component } from 'react';
import { connect } from 'react-redux';
import { Button } from '@material-ui/core';

import Grid from '@material-ui/core/Grid';
import Paper from '@material-ui/core/Paper';
import Typography from '@material-ui/core/Typography';

//imported house components
import overall from "./overallView.png";
import LightBulb from "./lightbulb.jpg";

import { fetchDevices, getHVAC } from "../../actions";


function DeviceList(props) {
  const rawList = props.devices

  console.log("DEVICES LIST")
  console.log(rawList);

  let deviceList = rawList.filter(device => {
    if(device.x === 0 && device.y === 0){
      return false
    }else{
      return true
    }
  }).map(device => {
    return (
      <img src={LightBulb} style={
        {
          top: device.y,
          left: device.x,
          width: '50px',
          position: 'absolute',
          opacity: device.state ? 1 : 0.5
        }
      } key={device.deviceId} />
    );
  })

  return <ul>{deviceList}</ul>;
}


class House extends Component {
  constructor(props) {
    super(props)

    const { dispatch } = this.props;
    dispatch(fetchDevices());
  }

  render() {
    return (
      <div style={
        {
          float: 'left',
          position: 'relative'
        }
      }>
        <img
          style={
            {
              verticalAlign: 'bottom'
            }
          }
          src={overall}
          style={{
            backgroundImage: `url(require("./houseComponents/overallView.png"))`,
            backgroundPosition: 'left',
            backgroundSize: '200px 200px'
          }} />

        <DeviceList devices={this.props.devicelist} />
      </div>
    );
  }
}

const mapStateToProps = state => {
  return {
    age: state.age,
    oven: state.oven,
    frontDoor: state.frontDoor,
    devices: state.devices,
    devicelist: state.devices.list,
    hvac: state.hvac
  };
};

const mapDispatchToProps = dispatch => {
  return {
    dispatch: dispatch
  };
};


export default connect(mapStateToProps, mapDispatchToProps)(House);
