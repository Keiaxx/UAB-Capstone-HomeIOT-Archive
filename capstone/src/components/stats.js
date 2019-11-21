import React, { useEffect, Component } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import Chart from 'react-apexcharts'

import { makeStyles } from '@material-ui/core/styles';
import Paper from '@material-ui/core/Paper';
import Grid from '@material-ui/core/Grid';
import Typography from '@material-ui/core/Typography';

const useStyles = makeStyles(theme => ({
  root: {
    flexGrow: 1,
  },
  paper: {
    padding: theme.spacing(2),
    textAlign: 'center',
    color: theme.palette.text.secondary,
  },
}));

class UsageGraph extends Component {

  constructor(props) {
    super(props);

    this.state = {
      options: {
        stroke: {
          curve: 'smooth'
        },
        markers: {
          size: 0
        },
        xaxis: {
          categories: ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        }
      },
      series: [{
        data: [30, 40, 25, 50, 49, 21, 70, 51]
      }],
    }
  }

  render() {

    return (
      <div className="line">
        <Chart options={this.state.options} series={this.state.series} type="line" width="100%" />
      </div>
    );
  }
}


export default function CenteredGrid() {
  const classes = useStyles();

  return (
    <div className={classes.root}>
      <Grid container spacing={3}>
        <Grid item xs={3}>
          <Paper className={classes.paper}>
            <Typography variant="h5" component="h3">
              Electricity
            </Typography>
            <Typography component="p">
              0 kWh
            </Typography>
          </Paper>
        </Grid>
        <Grid item xs={3}>
          <Paper className={classes.paper}>
            <Typography variant="h5" component="h3">
              Water
            </Typography>
            <Typography component="p">
              0 Gallons
            </Typography>
          </Paper>
        </Grid>
        <Grid item xs={3}>
          <Paper className={classes.paper}>
            <Typography variant="h5" component="h3">
              Total Cost To Date
            </Typography>
            <Typography component="p">
              $123
            </Typography>
          </Paper>
        </Grid>
        <Grid item xs={3}>
          <Paper className={classes.paper}>
            <Typography variant="h5" component="h3">
              Estimated Total
            </Typography>
            <Typography component="p">
              $400
            </Typography>
          </Paper>
        </Grid>

        <Grid item xs={12}>
          <Paper className={classes.paper}>
            <UsageGraph />
          </Paper>
        </Grid>

        <Grid item xs={6}>
          <Paper className={classes.paper}>
            <Typography variant="h5" component="h3">
              Average Daily Electricity Usage
            </Typography>
            <Typography component="p">
              100 kWh
            </Typography>
          </Paper>
        </Grid>

        <Grid item xs={6}>
          <Paper className={classes.paper}>
            <Typography variant="h5" component="h3">
              Average Daily Water Usage
            </Typography>
            <Typography component="p">
              100 Gallons
            </Typography>
          </Paper>
        </Grid>
      </Grid>
    </div>
  );
}