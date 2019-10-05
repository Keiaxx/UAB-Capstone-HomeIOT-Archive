
import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Typography from '@material-ui/core/Typography';


const useStyles = makeStyles({
  depositContext: {
    flex: 1,
  },
});

export default function Temp() {
  const classes = useStyles();
  return (
    <React.Fragment>
      <Typography component="p" variant="h6">
        INDOOR
        TEMP HERE
      </Typography>
    </React.Fragment>
  );
}