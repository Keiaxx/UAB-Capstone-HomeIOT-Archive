
import React, { Component } from 'react';
import { connect } from 'react-redux';
import Typography from '@material-ui/core/Typography';

import { fetchDevices, getHVAC } from "../../actions";

import Grid from '@material-ui/core/Grid';
import Container from '@material-ui/core/Container';
import { Button } from '@material-ui/core';


class Temp extends Component {
  constructor(props) {
    super(props)

    const { dispatch } = this.props;
    dispatch(getHVAC());
  }

  render() {
    return (
      <React.Fragment>
        <Grid container spacing={5}>
          <Grid item xs={4}>
            Int:
            <Typography component="p" variant="h2">
              {JSON.stringify(this.props.hvac.set_f)}
            </Typography>
          </Grid>
          <Grid item xs={4}>
            Ext:
            <Typography component="p" variant="h2">
              {JSON.stringify(this.props.hvac.set_f)}
            </Typography>
          </Grid>
          <Grid item xs={4}>
            Set:
            <Typography component="p" variant="h2">
              {JSON.stringify(this.props.hvac.set_f)}
            </Typography>
          </Grid>
          <Grid item xs={4}>
            <Button variant="contained" color="secondary"> + </Button><br />
            <Button variant="contained"> SET </Button> <br />
            <Button variant="contained" color="primary"> - </Button>
          </Grid>
        </Grid>
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