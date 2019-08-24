import React from 'react';
import withStyles from 'react-jss';
import "react-tabs/style/react-tabs.css";
import Switch from "react-switch";
import { GoDesktopDownload, GoCloudDownload } from 'react-icons/go';
import { style } from './style';
import Axios from 'axios';
import { CSVLink } from "react-csv";

class TabContent extends React.Component{
  constructor(props){
    super(props);
    this.state = {
      switch : true,
      timestamp : "Data as of "+new Date().toUTCString(),
      data : [],
      downloadData : []
    };
    this.updateTimeStamp = this.updateTimeStamp.bind(this);
    this.downloadFullData = this.downloadFullData.bind(this)
  }

  handleChange = () => {
    this.setState({switch : !this.state.switch})
  }

  updateTimeStamp () {
    if(this.state.switch){
      var _this_ = this;
      var t = new Date().toUTCString()
      this.setState({timestamp : "Data as of "+t})
      var limit = '50';
      Axios.get(this.props.dataURL+"/"+limit)
      .then(function(response){
        _this_.setState({data : response.data})
      })
      .catch(function(error){
        console.log(error)
        alert("Error while fetching data 1")
      })
    }
  }

  downloadFullData() {
    var _this_ = this;
    var limit = prompt("How many latest records you want to fetch ? ", "250");
    if(limit!=null){
      Axios.get(this.props.dataURL+"/"+limit)
      .then(function(response){
        _this_.setState({downloadData : response.data})
      })
      .catch(function(error){
        alert("Error while fetching data")
      })
    }
  }

  componentDidMount(){
    setInterval(this.updateTimeStamp, 5000)
  }

  render(){
    return(
      <React.Fragment>
        <div className={this.props.classes.body}>
          <div className={this.props.classes.statusRow}>
            <div className={this.props.classes.timeStamp}>
              {this.state.timestamp}
            </div>
            <div>
              { this.props.downloadFullData && <GoCloudDownload onClick={this.downloadFullData}/>}
              { this.props.downloadFullData && <CSVLink filename={"sharkaradar-"+this.state.timestamp+"-data.csv"} data={this.state.downloadData} separator={","}>
                <GoDesktopDownload/>
              </CSVLink>}
            </div>
            <div className={this.props.classes.switch}>
             Fetch data from Server every 5 seconds : <Switch onChange={this.handleChange} checked={this.state.switch} />
            </div>
          </div>
          <div className={this.props.classes.data}>
            {React.cloneElement(this.props.children, {rowdata : this.state.data})}
          </div>
        </div>
      </React.Fragment>
    )
  }
}

export default withStyles(style)(TabContent);
