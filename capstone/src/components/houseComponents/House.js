import React, { Component } from 'react';
import { connect } from 'react-redux';
import { makeStyles } from '@material-ui/core/styles';

//imported house components
import overall from "./overallView.png";
import LightBulb from "./lightbulb.jpg";

import { fetchDevices, setDeviceState } from "../../actions";


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
        } key={device.deviceId}/>
      );
  })

  return <ul>{deviceList}</ul>;
}

class House extends Component {
  constructor(props){
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
  
        <DeviceList devices={this.props.devicelist}/>
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
      devicelist: state.devices.list
  };
};

const mapDispatchToProps = dispatch => {
  return {
      dispatch: dispatch
  };
};


export default connect(mapStateToProps, mapDispatchToProps)(House);





/*
garage = 568 , 80
waterheater = 700, 180
washer and dryer = 840, 140
backdoor = 870, 20
oven = 935, 335
fridge = 920, 415
front door = 15, 710
bed1 (lights) = 100, 370
bed2 (lights) = 330, 370
bed3 (lights) = 700 , 370
bath (lights) = 540, 370
*/