import { csrfFetch } from './csrf';

export const postCarts = (carts) => {
    window.localStorage.setItem('ducksyCarts', JSON.stringify(carts));
}

const GET_CARTS = 'shoppingCart/GET_CARTS'

export const getCarts = (user = null) => async dispatch => {
    const cart_storage = window.localStorage.getItem('ducksyCarts');
    const carts = cart_storage ? JSON.parse(cart_storage) : {};
    if (!carts["guest"]) {
        carts["guest"] = {};
    }
    if (user) {
        if (!carts[user.id]) carts[user.id] = {}
    }
    postCarts(carts)
    dispatch({ type: GET_CARTS, carts })
    return carts
}

// const MERGE_CARTS = 'shoppingCart/MERGE_CARTS'
export const mergeCarts = (user_id) => async dispatch => {
    const carts = dispatch(getCarts())
    // Merge guest cart to log-in user cart
    carts[user_id] = Object.assign(carts[user_id], carts["guest"]);
    //  Clear guest cart
    carts["guest"] = {};
    dispatch({ type: GET_CARTS, carts })
}

export const deleteItem = (user_id, product_id) => async dispatch => {
    const carts = dispatch(getCarts())
    delete carts[user_id][product_id]
    postCarts()
    dispatch({ type: GET_CARTS, carts })
}

const UPDATE_CART = 'shoppingCart/UPDATE_CART'
const DELETE_CART = 'shoppingCart/DELETE_CART'



const initialState = window.localStorage.getItem('ducksy');

export default function ShoppingCartReducer(state = initialState, action) {
    switch (action.type) {
        case GET_CARTS:
            return action.carts
        default:
            return state
    }
}
