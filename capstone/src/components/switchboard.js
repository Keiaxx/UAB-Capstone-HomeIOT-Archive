import React, { Component } from 'react';
import { connect } from 'react-redux';

import Button from '@material-ui/core/Button';

class switchBoard extends Component {
    
      render(){
        return (
            <div className='swichboard'>
                <div className ='kitchen'>
                    <p>
                        Kitchen:<br/>
                            Oven: 
                            <Button  color="primary" onClick={this.props.TURNED_ON_OVEN}>ON</Button>
                            <Button  color="primary" onClick={this.props.TURNED_OFF_OVEN}>OFF</Button>
                            
                    </p>
                </div>
              
        
            </div>
          );
      }

}

//for every page you need a mapStateToProps for every component
const mapStateToProps = (state) => {
    return {
        age: state.age,
        oven: state.oven,
        frontDoor: state.frontDoor
    }
  }

//
const mapDispatchToProps = (dispatch) => {
return {
    TURNED_ON_OVEN: () => dispatch({type:'OVEN_ON'}),
    TURNED_OFF_OVEN: () => dispatch({type:'OVEN_OFF'})
}
}

  export default connect(mapStateToProps, mapDispatchToProps)(switchBoard);