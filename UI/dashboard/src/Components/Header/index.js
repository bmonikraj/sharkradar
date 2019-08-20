import React from 'react';
import withStyles from 'react-jss';
import { IoLogoGithub } from 'react-icons/io';
import { style } from './style';

const Header = ({children, classes, ...props}) => {
  return (
    <div className={classes.body}>
      <div className={classes.headerRow}>
        <span className={classes.brandName}>Sharkradar <small><em>[Service Registry and Discovery]</em></small> Dashboard </span>
        <span className={classes.forkOnGithub}>Fork on <a className={classes.forkOnGithubIcon} href="https://github.com/bmonikraj/sharkradar"><IoLogoGithub/></a></span>
      </div>
    </div>
  );
}

export default withStyles(style)(Header);
