import {createUseStyles} from 'react-jss';

export const style = theme => ({
	body : {
	  paddingBottom : '30px'
	},
  row : {
    display : 'flex'
  },
  column : {
    flex : '50%'
  },
  hostaddr : {
  	color : theme.colorPrimary + '!important',
  	fontWeight : 'bold'
  },
  header : {
  	color : theme.colorGreen + '!important',
  	fontWeight : 'bold',
  	fontSize : '18px' + '!important'
  },
  dataKey : {
  	fontStyle : 'italic' + '!important',
  	color : theme.colorTertiary + '!important',
  },
  dataValue : {
  	fontWeight : 'bold' + '!important',
  	color : theme.colorPrimary + '!important'
  },
  dataRow : {
  	paddingBottom : '1px',
  	paddinTop : '1px',
  	fontSize : '10px' + '!important'
  }
})
