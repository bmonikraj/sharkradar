import React from 'react';
import withStyles from 'react-jss';
import {
  PagingState,
  IntegratedPaging,
  FilteringState,
  IntegratedFiltering,
} from '@devexpress/dx-react-grid';
import {
  Grid,
  Table,
  TableHeaderRow,
  PagingPanel,
   TableFilterRow,
   TableColumnResizing,
} from '@devexpress/dx-react-grid-material-ui';
import Paper from '@material-ui/core/Paper';
import { style } from './style'

class TableServiceLogs extends React.Component{
  constructor(props){
    super(props)
    this.state = {
      rowdata : this.props.rowdata,
    }
  }

  render(){

    const columns = [
      {name : 'service_name', title: 'Name'},
      {name : 'ip', title: 'IP Address'},
      {name: 'port', title: 'Port'},
      {name: 'mem_usage', title: 'Mem Usage (%)'},
      {name: 'cpu_usage', title: 'CPU Usage (%)'},
      {name: 'nw_tput_bw_ratio', title: 'N/W TP B/W Ratio (%)'},
      {name: 'req_active_ratio', title: 'Active Request Ratio (%)'},
      {name: 'success_rate', title: 'Success Rate (%)'},
      {name: 'timestamp', title: 'Timestamp'},
      {name: 'health_interval', title: 'Health Interval (s)'},
    ]

    const defaultColumnWidths = [
      {columnName : 'service_name', width: 100},
      {columnName : 'ip', width: 100},
      {columnName: 'port', width: 100},
      {columnName: 'mem_usage', width: 100},
      {columnName: 'cpu_usage', width: 100},
      {columnName: 'nw_tput_bw_ratio', width: 100},
      {columnName: 'req_active_ratio', width: 100},
      {columnName: 'success_rate', width: 100},
      {columnName: 'timestamp', width: 100},
      {columnName: 'health_interval', width: 100},
    ]

    return(
      <React.Fragment>
        <div>
        <Paper>
            <Grid
              rows={this.state.rowdata}
              columns={columns}
            >
            <PagingState
              defaultCurrentPage={0}
              pageSize={5}
            />
            <IntegratedPaging />
            <FilteringState defaultFilters={[]} />
            <IntegratedFiltering />
            <Table />
            <TableColumnResizing defaultColumnWidths={defaultColumnWidths}/>
            <TableHeaderRow />
            <PagingPanel />
            <TableFilterRow />
          </Grid>
        </Paper>
        </div>
      </React.Fragment>
    )
  }

  componentWillReceiveProps(nextProps){
    if(this.props.rowdata !== nextProps.rowdata){
        this.setState({rowdata : nextProps.rowdata})
    }
  }
}

export default withStyles(style)(TableServiceLogs);
