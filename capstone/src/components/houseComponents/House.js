import React, { Component } from 'react';
import { connect } from 'react-redux';

//imported house components
import overall from "./overallView.png";
import LightBulb from "./lightbulb.jpg";

class House extends Component{

  render(){
    return(
      <div className='House'>
      <img 
      src={overall} 
      style={{
        backgroundImage: `url(require("./houseComponents/overallView.png"))`,
        backgroundPosition: 'left',
        backgroundSize: '200px 200px'
      }}/>
      {/*just checking here*/}
      {checkLights(this.props)}
      {this.props.oven[0]}<br/>
      {this.props.oven[1]}<br/>
      {this.props.oven[2]}<br/>
      </div>
    );
  }
}

function checkLights(props){
  const oven = props.oven[0];
  if(oven === "on"){ return (<img src={LightBulb} position="absolute" top={props.oven[1]} left = {props.oven[2]} /> )}
  const frontDoor = props.frontDoor[0];
  if(frontDoor === "on"){ return (<img src={LightBulb} position="absolute" top={props.frontDoor[1]} left = {props.frontDoor[2]} /> )}

}

//for every page you need a mapStateToProps for every component
const mapStateToProps = (state) => {
  return {
      oven: state.oven,
      frontDoor: state.frontDoor
  }
}


export default connect(mapStateToProps)(House);
