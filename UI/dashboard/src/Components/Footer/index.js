import React from 'react';
import withStyles from 'react-jss';
import { IoLogoGithub } from 'react-icons/io';
import { style } from './style';

const Footer = ({children, classes, ...props}) => {
  return (
    <div className={classes.body}>
      <p className={classes.contentMessage}><em>"Sharkradar"</em> is an Open Source project hosted on <a className={classes.hyperlink} href="https://bmonikraj.github.com/sharkradar">Github <IoLogoGithub/></a> <span className={classes.contentVersion}>[Current Version : v1.1.3]</span></p>
    </div>
  );
}

export default withStyles(style)(Footer);
