import React, { useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import ButtonAppBar from './AppBar';

function dashBoard() {
  
  const dispatch = useDispatch();
  

  return (
    <div className='LeaderBoard'>
      <ButtonAppBar/>
            
    </div>
  );
}

export default dashBoard;