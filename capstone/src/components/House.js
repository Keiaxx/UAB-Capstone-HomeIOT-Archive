import React, { useEffect } from 'react';

//imported house components
import overall from "./houseComponents/overallView.png";
import LightBulb from "./houseComponents/lightbulb.jpg";

import { useSelector, useDispatch } from 'react-redux';

function House() { 
  const hw = 40;
  const name = "waterHeater";
  const dispatch = useDispatch();

  function paintHouse(name){
    switch(name){
      case "garage1":
        return <img src={LightBulb} height={hw} width={hw} style={{position:'absolute', top:'130px', left:'500px'}}/>
      case"garage2":
        return <img src={LightBulb} height={hw} width={hw} style={{position:'absolute', top:'230px', left:'500px'}}/>
      case"waterHeater":
        return <img src={LightBulb} height={hw} width={hw} style={{position:'absolute', top:'210px', left:'790px'}}/>
      case"win1":
        return <img src={LightBulb} height={hw} width={hw} style={{position:'absolute', top:'230px', left:'500px'}}/>
      case"win2":
        return <img src={LightBulb} height={hw} width={hw} style={{position:'absolute', top:'230px', left:'500px'}}/>
      case"win3":
        return <img src={LightBulb} height={hw} width={hw} style={{position:'absolute', top:'230px', left:'500px'}}/>
      case"washer":
        return <img src={LightBulb} height={hw} width={hw} style={{position:'absolute', top:'230px', left:'500px'}}/>
      case"dryer":
        return <img src={LightBulb} height={hw} width={hw} style={{position:'absolute', top:'230px', left:'500px'}}/>
      case"frontD":
        return <img src={LightBulb} height={hw} width={hw} style={{position:'absolute', top:'230px', left:'500px'}}/>
      case"backD":
        return <img src={LightBulb} height={hw} width={hw} style={{position:'absolute', top:'230px', left:'500px'}}/>
      case"refridge":
        return <img src={LightBulb} height={hw} width={hw} style={{position:'absolute', top:'230px', left:'500px'}}/>
      case"stove":
        return <img src={LightBulb} height={hw} width={hw} style={{position:'absolute', top:'230px', left:'500px'}}/>
      case"HVAC":
        return <img src={LightBulb} height={hw} width={hw} style={{position:'absolute', top:'230px', left:'500px'}}/>
      case"tv":
        return <img src={LightBulb} height={hw} width={hw} style={{position:'absolute', top:'230px', left:'500px'}}/>
        default:
          //code here
    }
  }
  
  return (
    <div className='House'>
      <img 
      src={overall} 
      style={{
        backgroundImage: `url(require("./houseComponents/overallView.png"))`,
        backgroundPosition: 'left',
        backgroundSize: '200px 200px'
      }}/>
      {paintHouse(name)}
    </div>
  );
}

export default House;