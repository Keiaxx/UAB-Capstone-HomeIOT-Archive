
import React, { Component } from 'react';
import { connect } from 'react-redux';
import Typography from '@material-ui/core/Typography';

import { fetchDevices, getHVAC } from "../../actions";


class Temp extends Component {
  constructor(props) {
    super(props)

    const { dispatch } = this.props;
    dispatch(getHVAC());
  }

  render(){
    return (
      <React.Fragment>
        <Typography component="p" variant="h6">
        {JSON.stringify(this.props.hvac.set_f)}      
        </Typography>
      </React.Fragment>
    );
  }
}


const mapStateToProps = state => {
  return {
    hvac: state.hvac
  };
};

const mapDispatchToProps = dispatch => {
  return {
    dispatch: dispatch
  };
};

export default connect(mapStateToProps, mapDispatchToProps)(Temp);