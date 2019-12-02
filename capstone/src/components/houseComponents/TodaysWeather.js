
import React, { Component } from 'react';
import { connect } from 'react-redux';
import Typography from '@material-ui/core/Typography';

import { fetchDevices, getHVAC, setHVAC } from "../../actions";

import Grid from '@material-ui/core/Grid';
import Container from '@material-ui/core/Container';
import { Button } from '@material-ui/core';

class Temp extends Component {
  constructor(props) {
    super(props)

    const { dispatch } = this.props;

    dispatch(getHVAC());
  }

  addOne(set_f, low_f, high_f) {
    console.log("ADDING ONE")

    const { dispatch } = this.props;
    dispatch(setHVAC(set_f, low_f, high_f));

  }

  subOne(set_f, low_f, high_f) {
    console.log("SUBTRACTING ONE")

    const { dispatch } = this.props;
    dispatch(setHVAC(set_f, low_f, high_f));

  }

  render() {

    return (
      <React.Fragment>
        <Grid container spacing={5}>

          <Grid item xs={4}>
            Low:
            <Typography component="p" variant="h2">
              {JSON.stringify(this.props.hvac.low_f)}
            </Typography>
          </Grid>
          <Grid item xs={4}>
            Set:
            <Typography component="p" variant="h2">
              {JSON.stringify(this.props.hvac.set_f)}
            </Typography>
          </Grid>
          <Grid item xs={4}>
            High:
            <Typography component="p" variant="h2">
              {JSON.stringify(this.props.hvac.high_f)}
            </Typography>
          </Grid>

          <Grid item xs={4}>
            <Button variant="contained" color="secondary" onClick={(e) => {
              this.props.hvac.low_f++
              this.addOne(this.props.hvac.set_f, this.props.hvac.low_f, this.props.hvac.high_f)
            }
            }> + </Button><br />
            <Button variant="contained"> SET </Button> <br />
            <Button variant="contained" color="primary" onClick={(e) => {
              this.props.hvac.low_f--
              this.subOne(this.props.hvac.set_f, this.props.hvac.low_f, this.props.hvac.high_f)
            }
            } > - </Button>
          </Grid>
          <Grid item xs={4}>
            <Button variant="contained" color="secondary" onClick={(e) => {
              this.props.hvac.set_f++
              this.addOne(this.props.hvac.set_f, this.props.hvac.low_f, this.props.hvac.high_f)
            }
            }> + </Button><br />
            <Button variant="contained"> SET </Button> <br />
            <Button variant="contained" color="primary" onClick={(e) => {
              this.props.hvac.set_f--
              this.subOne(this.props.hvac.set_f, this.props.hvac.low_f, this.props.hvac.high_f)
            }
            } > - </Button>
          </Grid>
          <Grid item xs={4}>
            <Button variant="contained" color="secondary" onClick={(e) => {
              this.props.hvac.high_f++
              this.addOne(this.props.hvac.set_f, this.props.hvac.low_f, this.props.hvac.high_f)
            }
            }> + </Button><br />
            <Button variant="contained"> SET </Button> <br />
            <Button variant="contained" color="primary" onClick={(e) => {
              this.props.hvac.high_f--
              this.subOne(this.props.hvac.set_f, this.props.hvac.low_f, this.props.hvac.high_f)
            }
            } > - </Button>
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