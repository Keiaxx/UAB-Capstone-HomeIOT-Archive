import React, { Component } from 'react';
import { connect } from 'react-redux';
import { Button } from '@material-ui/core';
import { makeStyles } from '@material-ui/core/styles';

//imported house components
import overall from "./overallView.png";
import LightBulb from "./lightbulb.jpg";

import { fetchDevices, getHVAC } from "../../actions";


function DeviceList(props) {
  const rawList = props.devices

  console.log("DEVICES LIST")
  console.log(rawList);

  let deviceList = rawList.map(device => {
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
          <Button variant="contained" color="secondary"> +   </Button><br/>
          <Button variant="contained"> SET </Button> <br/>
          <Button variant="contained" color="primary"> - </Button>
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

        {JSON.stringify(this.props.hvac.set_f)}
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
