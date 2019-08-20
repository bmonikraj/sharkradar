import React from 'react';
import withStyles from 'react-jss';
import { Tab, Tabs, TabList, TabPanel } from 'react-tabs';
import "react-tabs/style/react-tabs.css";
import TabContent from '../TabContent/index';
import { style } from './style';

const Panel = ({children, classes, ...props}) => {
  return (
    <div className={classes.body}>
      <Tabs>
        <TabList>
            <Tab><span className={classes.tabTitle}>Real Time Monitor</span></Tab>
            <Tab><span className={classes.tabTitle}>Discovery Monitor Logs</span></Tab>
            <Tab><span className={classes.tabTitle}>Service Monitor Logs</span></Tab>
        </TabList>
    
        <TabPanel>
            <TabContent children={<h1>Hello 1</h1>}/>
        </TabPanel>
        <TabPanel>
            <TabContent children={<h1>Hello 2</h1>}/>
        </TabPanel>
        <TabPanel>
            <TabContent children={<h1>Hello 3</h1>}/>
        </TabPanel>
    </Tabs>
    </div>
  );
}

export default withStyles(style)(Panel);
