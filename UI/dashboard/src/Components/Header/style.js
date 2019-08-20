import {createUseStyles} from 'react-jss';

export const style = theme => ({
  
  body : {
    background : theme.colorSecondary,
    position : 'relative',
    top : '0px',
    left : '0px',
    width : '100%',
  },

  headerRow : {
    display : 'flex',
    justifyContent : 'space-between',
    padding : '20px'
  },

  brandName : {
    color : theme.colorPrimary,
    fontSize : '24px',
    fontWeight : 'bold'
  },

  forkOnGithub : {
    color : theme.colorPrimary,
    fontSize : '24px',
    fontWeight : 'bold',
    border : 'solid',
    borderColor : theme.colorPrimary,
    borderWidth : '1px',
    padding : '5px'
  },

  forkOnGithubIcon : {
    color : theme.colorPrimary,
    fontSize : '24px',
    fontWeight : 'bold',
    padding : '5px'
  }
})
