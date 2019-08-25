import React from 'react';
import withStyles from 'react-jss';
import { Tab, Tabs, TabList, TabPanel } from 'react-tabs';
import "react-tabs/style/react-tabs.css";
import TabContent from '../TabContent/index';
import { style } from './style';
import TableDiscoveryLogs from '../TableDiscoveryLogs/index';
import TableServiceLogs from '../TableServiceLogs/index';
import CardsRealTime from '../CardsRealTime/index';

const Panel = ({children, classes, ...props}) => {
  return (
    <div className={classes.body}>
      <Tabs>
        <TabList>
            <Tab><span className={classes.tabTitle}>Real Time Monitor</span></Tab>
            <Tab><span className={classes.tabTitle}>Service Monitor Logs</span></Tab>
            <Tab><span className={classes.tabTitle}>Discovery Monitor Logs</span></Tab>
        </TabList>

        <TabPanel>
            <TabContent children={<CardsRealTime/>} downloadFullData={false} dataURL={"/monitor-real-time/current"}/>
        </TabPanel>
        <TabPanel>
            <TabContent children={<TableServiceLogs/>} downloadFullData={true} dataURL={"/monitor-real-time/service"}/>
        </TabPanel>
        <TabPanel>
            <TabContent children={<TableDiscoveryLogs/>} downloadFullData={true} dataURL={"/monitor-real-time/discovery"}/>
        </TabPanel>
    </Tabs>
    </div>
  );
}

export default withStyles(style)(Panel);
