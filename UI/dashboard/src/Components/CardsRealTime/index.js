import React from 'react';
import withStyles from 'react-jss';
import { Card } from 'semantic-ui-react'
import { style } from './style'
import 'semantic-ui-css/semantic.min.css'

class CardsRealTime extends React.Component{
  constructor(props){
    super(props)
    this.state = {
      rowdata : this.props.rowdata,
    }
  }

  render(){

    return(
      <React.Fragment>
        <div>
        <Card.Group>
        {
          this.state.rowdata.map((data, index) => {
            return(
              <Card>
                <Card.Content header={data['service_name']} />
                <Card.Content description={'Host Address : '+data['ip']+':'+data['port']} />
                <Card.Content extra>
                  <div className={this.props.classes.row}>
                    <div className={this.props.classes.column}>
                      <p>Mem Usage (%) - {data['mem_usage']}</p>
                      <p>CPU Usage (%) - {data['cpu_usage']}</p>
                      <p>NW TP BW ratio (%) - {data['nw_tput_bw_ratio']}</p>
                    </div>
                    <div className={this.props.classes.column}>
                      <p>Active Request Ratio (%) - {data['req_active_ratio']}</p>
                      <p>Success Rate (%) - {data['Success Rate']}</p>
                      <p>Health Interval (s) - {data['health_interval']}</p>
                    </div>
                  </div>
                </Card.Content>
              </Card>
            )
          })
        }
        </Card.Group>
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

export default withStyles(style)(CardsRealTime);
