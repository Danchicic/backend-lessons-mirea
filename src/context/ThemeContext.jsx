import React, {createContext, useState, useEffect} from 'react';
import {createTheme, ThemeProvider} from '@mui/material/styles';


// Helper function to validate the theme mode
const getValidMode = (mode) => {
    return mode === 'light' || mode === 'dark' ? mode : 'light';
};

export const ThemeContext = createContext();

export const ThemeContextProvider = ({children}) => {
    // Initialize mode with a valid value from localStorage or default to 'light'
    const [mode, setMode] = useState(getValidMode(localStorage.getItem('theme')));

    // Save the current mode to localStorage whenever it changes
    useEffect(() => {
        localStorage.setItem('theme', mode);
    }, [mode]);

    // Toggle between light and dark modes
    const toggleTheme = () => {
        setMode((prevMode) => (prevMode === 'light' ? 'dark' : 'light'));
    };

    // Create the theme dynamically based on the mode
    const theme = createTheme({
        palette: {
            mode, // Use the validated mode
            primary: {
                main: '#1976d2',
            },
            secondary: {
                main: '#dc004e',
            },
        },
    });

    return (
        <ThemeContext.Provider value={{toggleTheme, mode}}>
            <ThemeProvider theme={theme}>{children}</ThemeProvider>
        </ThemeContext.Provider>
    );
};