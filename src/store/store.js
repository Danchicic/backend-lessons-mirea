import { configureStore } from '@reduxjs/toolkit';
import productsReducer from '../features/productsSlice';
import CartSlice from "../features/cartSlice.js";
export const store = configureStore({
    reducer: {
        products: productsReducer,
        cart:CartSlice,
    },
});