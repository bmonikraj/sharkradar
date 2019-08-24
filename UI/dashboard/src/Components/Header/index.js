import React from 'react';
import withStyles from 'react-jss';
import { IoMdBookmarks } from 'react-icons/io';
import { style } from './style';

const Header = ({children, classes, ...props}) => {
  return (
    <div className={classes.body}>
      <div className={classes.headerRow}>
        <span className={classes.brandName}>Sharkradar <small><em>[Service Registry and Discovery]</em></small> Dashboard </span>
        <span className={classes.documentation}><a href="https://bmonikraj.github.io/sharkradar">Documentation <IoMdBookmarks/></a></span>
      </div>
    </div>
  );
}

export default withStyles(style)(Header);
