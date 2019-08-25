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
        <div className={this.props.classes.body}>
        <Card.Group>
        {
          this.state.rowdata.map((data, index) => {
            return(
              <Card>
                <Card.Content extra className={this.props.classes.header}>
                  {data['service_name']}
                </Card.Content>
                <Card.Content extra className={this.props.classes.hostaddr}>
                  {data['ip']+':'+data['port']}
                </Card.Content>
                <Card.Content extra>
                  <div className={this.props.classes.row}>
                    <div className={this.props.classes.column}>
                      <p className={this.props.classes.dataRow}><span className={this.props.classes.dataKey}>Mem Usage (%) -</span> <span className={this.props.classes.dataValue}>{data['mem_usage']}</span></p>
                      <p className={this.props.classes.dataRow}><span className={this.props.classes.dataKey}>CPU Usage (%) -</span> <span className={this.props.classes.dataValue}>{data['cpu_usage']}</span></p>
                      <p className={this.props.classes.dataRow}><span className={this.props.classes.dataKey}>NW TP BW ratio (%) -</span> <span className={this.props.classes.dataValue}>{data['nw_tput_bw_ratio']}</span></p>
                    </div>
                    <div className={this.props.classes.column}>
                      <p className={this.props.classes.dataRow}><span className={this.props.classes.dataKey}>Active Request Ratio (%) -</span> <span className={this.props.classes.dataValue}>{data['req_active_ratio']}</span></p>
                      <p className={this.props.classes.dataRow}><span className={this.props.classes.dataKey}>Success Rate (%) -</span> <span className={this.props.classes.dataValue}>{data['success_rate']}</span></p>
                      <p className={this.props.classes.dataRow}><span className={this.props.classes.dataKey}>Health Interval (s) -</span> <span className={this.props.classes.dataValue}>{data['health_interval']}</span></p>
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
