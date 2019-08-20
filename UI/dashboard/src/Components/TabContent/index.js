import React from 'react';
import withStyles from 'react-jss';
import { Tab, Tabs, TabList, TabPanel } from 'react-tabs';
import "react-tabs/style/react-tabs.css";
import { style } from './style';

const TabContent = ({children, classes, ...props}) => {
  return (
    <div className={classes.body}>
      {children}
    </div>
  );
}

export default withStyles(style)(TabContent);
