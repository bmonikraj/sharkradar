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

class TableDiscoveryLogs extends React.Component{
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
      {name: 'timestamp', title: 'Timestamp'},
      {name: 'status', title: 'Status'},
      {name: 'retry_id', title: 'Retry ID'}
    ]

    const defaultColumnWidths = [
      {columnName : 'service_name', width: 200},
      {columnName : 'ip', width: 200},
      {columnName: 'port', width: 200},
      {columnName: 'status', width: 200},
      {columnName: 'timestamp', width: 200},
      {columnName: 'retry_id', width: 200},
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

export default withStyles(style)(TableDiscoveryLogs);
