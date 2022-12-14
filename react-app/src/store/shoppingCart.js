import { csrfFetch } from './csrf';

const GET_CARTS = 'shoppingCart/GET_CARTS'

export const getCarts = () => async dispatch => {
    const carts = window.localStorage.getItem('ducksy');
    dispatch({ type: GET_CARTS, carts })
}

export const mergeCarts = () => async disptach => {

}

const MERGE_CARTS = 'shoppingCart/MERGE_CARTS'
const UPDATE_CART = 'shoppingCart/UPDATE_CART'
const DELETE_CART = 'shoppingCart/UPDATE_CART'



const initialState = window.localStorage.getItem('ducksy');

export default function ShoppingCartReducer(state = initialState, action) {
    switch (action.type) {
        case GET_CARTS:
            return action.carts

    }
}
