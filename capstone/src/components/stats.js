import React, { Fragment, useState, useEffect, Component } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import Chart from 'react-apexcharts'

import { makeStyles, withStyles } from '@material-ui/core/styles';
import Paper from '@material-ui/core/Paper';
import Grid from '@material-ui/core/Grid';
import Typography from '@material-ui/core/Typography';

import MomentUtils from '@date-io/moment';
import { MuiPickersUtilsProvider } from '@material-ui/pickers';
import { DatePicker } from "@material-ui/pickers";
import * as moment from 'moment';
import API from '../services/api';

//TODO: Round numbers
//TODO: Change date picker to true month instead of going back one

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

class YearMonthPicker extends Component {

  state = { date: Date.now() };

  handleDateChange = (date) => {
    this.setState({ date });
    this.props.onDateChanged(date)
  };

  constructor(props) {
    super(props)
  }

  render() {
    return (
      <Fragment>
        <DatePicker
          openTo="year"
          views={["year", "month"]}
          label="Year and Month"
          helperText="Start from year selection"
          value={this.state.date}
          onChange={this.handleDateChange}
        />
      </Fragment>
    );
  }
}

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
          type: 'datetime',
        },
      }
    }
  }

  render() {

    return (
      <div className="line">
        <Chart options={this.state.options} series={this.props.series} type="line" width="100%" />
      </div>
    );
  }
}

class StatsPage extends Component {

  constructor(props) {
    super(props);

    this.state = {
      selected_date: new Date(),
      usagedata: {
        electricity: {
          kwh: 10,
        },
        water: {
          gallons: 0,
        },
        eom_predictions: {
          water: 0,
          electricity: 0,
        },
        average_daily: {
          electricity: 0,
          water: 0,
        }
      },
      graph: [
        {
          data: []
        },
        {
          data: []
        },
        {
          data: []
        },
        {
          data: []
        }
      ]
    }
  }

  componentDidMount() {
    this.loadStatistics(new Date())
  }

  kwh_to_dollars = (kwh) => kwh * 0.12
  ft3_to_dollars = (ft3) => {
    let gals = (2.52 / 100) * ft3
    console.log(gals)
    return gals
  }
  calculate_current_cost = () => this.kwh_to_dollars(this.state.usagedata.electricity.kwh) + this.ft3_to_dollars(this.state.usagedata.water.gallons)
  calculate_estimated_cost = () => this.kwh_to_dollars(this.state.usagedata.eom_predictions.electricity) + this.ft3_to_dollars(this.state.usagedata.eom_predictions.water)

  // Handle month change events
  loadStatistics(date) {
    console.log(date)

    let currdate = moment(date).subtract(1, 'months').startOf('month')
    let isostring = currdate.format("YYYY-MM-DD")

    API.get(`usage/usagestats?start=${isostring}`)
      .then(
        response => response.data,
        error => console.log('An error occurred.', error)
      )
      .then(json => {
        console.log(json)
        let stats = json.stats
        let graphing = json.graphing

        this.setState({
          selected_date: this.state.selected_date,
          usagedata: {
            electricity: {
              kwh: stats.totals.electricity,
            },
            water: {
              gallons: stats.totals.water,
            },
            eom_predictions: {
              water: graphing.month_end_predict.water,
              electricity: graphing.month_end_predict.electric,
            },
            average_daily: {
              electricity: stats.dailyaverage.electricity,
              water: stats.dailyaverage.water,
            }
          },
          graph: [
            {
              name: 'Daily Electric (kWh)',
              data: graphing.electric.raw,
            },
            {
              name: 'Daily Water (Gals)',
              data: graphing.water.raw,
            },
            {
              name: 'Electric Running Total',
              data: graphing.electric.runningtotal,
            },
            {
              name: 'Water Running Total',
              data: graphing.water.runningtotal,
            }
          ]
        });
      })

  }

  render() {
    const { classes } = this.props;
    const current_cost = this.calculate_current_cost()
    const predicted_cost = this.calculate_estimated_cost()


    return (
      <div className={classes.root}>
        <Grid container spacing={3}>
          <Grid item xs={3}>
            <Paper className={classes.paper}>
              <Typography variant="h5" component="h3">
                Choose Month
            </Typography>
              <MuiPickersUtilsProvider utils={MomentUtils}>
                <YearMonthPicker onDateChanged={this.loadStatistics}></YearMonthPicker>
              </MuiPickersUtilsProvider>
            </Paper>
          </Grid>
          <Grid item xs={3}>
            <Paper className={classes.paper}>
              <Typography variant="h5" component="h3">
                Electricity
            </Typography>
              <Typography component="p">
                {this.state.usagedata.electricity.kwh} kWh
            </Typography>
            </Paper>
          </Grid>
          <Grid item xs={3}>
            <Paper className={classes.paper}>
              <Typography variant="h5" component="h3">
                Water
            </Typography>
              <Typography component="p">
                {this.state.usagedata.water.gallons} ft^3
            </Typography>
            </Paper>
          </Grid>
          <Grid item xs={3}>
            <Paper className={classes.paper}>
              <Typography variant="h5" component="h3">
                Total Cost To Date
            </Typography>
              <Typography component="p">
                ${current_cost}
              </Typography>
            </Paper>
          </Grid>
          <Grid item xs={3}>
            <Paper className={classes.paper}>
              <Typography variant="h5" component="h3">
                Estimated Total
            </Typography>
              <Typography component="p">
                ${predicted_cost}
              </Typography>
            </Paper>
          </Grid>

          <Grid item xs={12}>
            <Paper className={classes.paper}>
              <UsageGraph series={this.state.graph} />
            </Paper>
          </Grid>

          <Grid item xs={6}>
            <Paper className={classes.paper}>
              <Typography variant="h5" component="h3">
                Average Daily Electricity Usage
            </Typography>
              <Typography component="p">
                {this.state.usagedata.average_daily.electricity} kWh
            </Typography>
            </Paper>
          </Grid>

          <Grid item xs={6}>
            <Paper className={classes.paper}>
              <Typography variant="h5" component="h3">
                Average Daily Water Usage
            </Typography>
              <Typography component="p">
                {this.state.usagedata.average_daily.water} ft^3
            </Typography>
            </Paper>
          </Grid>
        </Grid>
      </div>
    );
  }
}


export default withStyles(useStyles)(StatsPage)