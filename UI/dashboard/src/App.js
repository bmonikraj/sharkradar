import React from 'react';
import { ThemeProvider } from 'react-jss';
import { MainTheme } from './Theme.js';
import Dashboard from './Components/Dashboard/index';

export const App = () => {
  return (
      <ThemeProvider theme={MainTheme}>
        <Dashboard/>
      </ThemeProvider>
    );
}
