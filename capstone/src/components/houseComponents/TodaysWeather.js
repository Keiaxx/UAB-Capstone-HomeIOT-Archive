
import React from 'react';
import { connect } from 'react-redux';
import Typography from '@material-ui/core/Typography';




function Temp() {
  
  return (
    <React.Fragment>
      <Typography component="p" variant="h6">
        INDOOR
        TEMP HERE
      </Typography>
    </React.Fragment>
  );
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

export default connect(mapStateToProps, mapDispatchToProps)(Temp);