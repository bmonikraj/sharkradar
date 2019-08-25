import {createUseStyles} from 'react-jss';

export const style = theme => ({
  
  body : {
    background : theme.colorTertiary,
    position : 'fixed',
    bottom : '0px',
    left : '0px',
    width : '100%'
  },

  contentMessage : {
    color : theme.colorPrimary,
    fontSize : '16px',
    fontWeight : 'bold',
    textAlign : 'center'
  },

  contentVersion : {
    color : theme.colorPrimary,
    fontSize : '14px',
    fontWeight : 'normal',
    textAlign : 'center'
  },

  hyperlink : {
    color : theme.colorPrimary
  }
})
