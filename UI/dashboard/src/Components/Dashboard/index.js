import React from 'react';
import withStyles from 'react-jss';
import { style } from './style';
import Header from '../Header/index';
import Footer from '../Footer/index';

const Dashboard = ({children, classes, ...props}) => {
  return (
    <div className={classes.background}>
      <Header/>
      <Footer/>
    </div>
  );
}

export default withStyles(style)(Dashboard);
