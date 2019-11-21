import React, { Component } from 'react';
import { connect } from 'react-redux';
import { makeStyles } from '@material-ui/core/styles';

//imported house components
import overall from "./overallView.png";
import LightBulb from "./lightbulb.jpg";

const useStyles = makeStyles(theme => ({
  housediv: {
    float: 'left',
    position: 'relative'
  },
  houseimage: {
    verticalAlign: 'bottom'
  },
  lightbulb: {
    top: 0,
    left: 0,
    position: 'absolute'
  }
}))

function House() {
  let classes = useStyles();

  return (
    <div className={classes.housediv}>
      <img
        className={classes.houseimage}
        src={overall}
        style={{
          backgroundImage: `url(require("./houseComponents/overallView.png"))`,
          backgroundPosition: 'left',
          backgroundSize: '200px 200px'
        }} />

      <img src={LightBulb} style={
        {
          top: 275,
          left: 50,
          width: '50px',
          position: 'absolute'
        }
      } />

      <img src={LightBulb} style={
        {
          top: 150,
          left: 600,
          width: '50px',
          position: 'absolute'
        }
      } />
    </div>
  );
}


function checkLights(props) {
  const oven = props.oven[0];
  if (oven === "on") { return (<img src={LightBulb} position="absolute" top={props.oven[1]} left={props.oven[2]} />) }
  const frontDoor = props.frontDoor[0];
  if (frontDoor === "on") { return (<img src={LightBulb} position="absolute" top={props.frontDoor[1]} left={props.frontDoor[2]} />) }

}

//for every page you need a mapStateToProps for every component
const mapStateToProps = (state) => {
  return {
    oven: state.oven,
    frontDoor: state.frontDoor
  }
}


export default connect(mapStateToProps)(House);
