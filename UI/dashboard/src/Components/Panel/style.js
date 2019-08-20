import {createUseStyles} from 'react-jss';

export const style = theme => ({
  body : {
    background : theme.colorBackground,
    margin : '5px'
  },
  tabTitle : {
    color : theme.colorSecondary,
    textTransform : 'uppercase'
  }
})
