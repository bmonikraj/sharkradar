import {createUseStyles} from 'react-jss';

export const style = theme => ({
  body : {
      background : theme.colorBackground,
      padding : '2px'
  },
  statusRow : {
    display : 'flex',
    justifyContent : 'space-between',
    marginBottom : '20px',
    marginTop : '10px'
  },
  download : {
    display : 'flex',
    justifyContent : 'space-between',
  },
  downloadIcon : {
    paddingLeft : '5px',
    paddingRight : '5px',
    cursor : 'pointer',
    color : theme.colorPrimary,
    '& a' : {
      color : theme.colorPrimary
    }
  },
  timeStamp : {
    color : theme.colorTertiary
  },
  switch : {
    color : theme.colorTertiary,
    marginTop : '-15px'
  },
  boldtext : {
    fontWeight : 'bold'
  },
  data : {

  }
})
