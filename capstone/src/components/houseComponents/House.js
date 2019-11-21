import React, { Component } from 'react';
import { connect } from 'react-redux';
import { makeStyles } from '@material-ui/core/styles';

//imported house components
import overall from "./overallView.png";
import LightBulb from "./lightbulb.jpg";

const devicesloc = [
  {
    name: 'garage',
    x: 568,
    y: 80
  },
  {
    name: 'waterheater',
    x: 700,
    y: 180
  },
  {
    name: 'washerdryer',
    x: 840,
    y: 140
  },
  {
    name: 'backdoor',
    x: 870,
    y: 20
  },
  {
    name: 'oven',
    x: 935,
    y: 335
  },
  {
    name: 'fridge',
    x: 920,
    y: 415
  },
  {
    name: 'frontdoor',
    x: 15,
    y: 710
  },
  {
    name: 'bed1',
    x: 100,
    y: 370
  },
  {
    name: 'bed2',
    x: 330,
    y: 370
  },
  {
    name: 'bed3',
    x: 700,
    y: 370
  },
  {
    name: 'bath',
    x: 540,
    y: 370
  },
]

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
  let items = []

  for (let it in devicesloc) {
    let device = devicesloc[it]

    items.push(<img src={LightBulb} style={
      {
        top: device.y,
        left: device.x,
        width: '50px',
        position: 'absolute'
      }
    } />)
  }

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



      {items}
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