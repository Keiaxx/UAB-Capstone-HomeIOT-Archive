import React, { useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
//material-ui imports
import clsx from 'clsx';
import { makeStyles } from '@material-ui/core/styles';
import Paper from '@material-ui/core/Paper';
import Grid from '@material-ui/core/Grid';
import Container from '@material-ui/core/Container';
import Fab from '@material-ui/core/Fab';
import AddIcon from '@material-ui/icons/Add';

//component imports
import ButtonAppBar from './AppBar';
import House from './houseComponents/House';
import Temp from './houseComponents/TodaysWeather';

const drawerWidth = 240;


const useStyles = makeStyles(theme => ({
  root: {
    display: 'flex-grow',
  },
  title: {
    flexGrow: 1,
  },
  drawerPaper: {
    position: 'relative',
    whiteSpace: 'nowrap',
    width: drawerWidth,
    transition: theme.transitions.create('width', {
      easing: theme.transitions.easing.sharp,
      duration: theme.transitions.duration.enteringScreen,
    }),
  },
  drawerPaperClose: {
    overflowX: 'hidden',
    transition: theme.transitions.create('width', {
      easing: theme.transitions.easing.sharp,
      duration: theme.transitions.duration.leavingScreen,
    }),
    width: theme.spacing(7),
    [theme.breakpoints.up('sm')]: {
      width: theme.spacing(9),
    },
  },
  content: {
    flexGrow: 1,
    height: '100vh',
    overflow: 'auto',
  },
  container: {
    paddingTop: theme.spacing(2),
    paddingBottom: theme.spacing(2),
  },
  paper: {
    padding: theme.spacing(2),
    display: 'flex',
    overflow: 'auto',
    flexDirection: 'column',
  },
  fixedHeight: {
    height: 200,
  }
}));

function Dashboard() {
  const classes = useStyles();
  const fixedHeightPaper = clsx(classes.paper, classes.fixedHeight);

  return (
    <div className={classes.root}>
      <Container className={classes.container}>
        <ButtonAppBar />
        <Grid item xs={6} md={4} lg={3}>
          <Paper className={fixedHeightPaper}>
            <Temp />
          </Paper>
          <Fab color="primary" aria-label="add" className={classes.fab}>
            <AddIcon />
          </Fab>
          <Fab color="extended" aria-label="add" className={classes.fab}>
            <AddIcon />
          </Fab>          
          <Fab style={{backgroundColor:'red'}} aria-label="add" className={classes.fab}>
            <AddIcon />
          </Fab>
          <House />
        </Grid>
      </Container>
    </div>
  );
}

export default Dashboard;
