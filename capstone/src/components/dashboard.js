import React, { useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import ButtonAppBar from './AppBar';
import House from './House';

function Dashboard() {
  
  const dispatch = useDispatch();
  

  return (
    <div className='LeaderBoard'>
      <ButtonAppBar/>
      <House/>
    </div>
  );
}

export default Dashboard;