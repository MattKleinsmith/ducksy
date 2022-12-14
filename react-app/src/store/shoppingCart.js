export const saveCarts = (carts) => {
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
    saveCarts(carts)
    dispatch({ type: GET_CARTS, carts })
    return carts
}

export const mergeCarts = (user_id) => async dispatch => {
    const carts = await dispatch(getCarts())
    // Merge guest cart to log-in user cart
    carts[user_id] = Object.assign(carts[user_id], carts["guest"]);
    //  Clear guest cart
    carts["guest"] = {};
    saveCarts(carts)
    dispatch({ type: GET_CARTS, carts })
}

export const addItemToCart = (product, user) => async dispatch => {
    const carts = await dispatch(getCarts())
    const current_cart = user ? carts[user.id] : carts['guest'];
    if (String(product.id) in current_cart) current_cart[product.id] += 1;
    else current_cart[product.id] = 1;
    console.log(carts)
    saveCarts(carts)
    dispatch({ type: GET_CARTS, carts })
};

export const deleteItemFromCart = (product, user) => async dispatch => {
    const carts = await dispatch(getCarts())
    const current_cart = user ? carts[user.id] : carts['guest'];
    delete current_cart[product.id]
    console.log("delete item from cart", current_cart)
    saveCarts(carts)
    dispatch({ type: GET_CARTS, carts })
}


const initialState = window.localStorage.getItem('ducksy');

export default function ShoppingCartReducer(state = initialState, action) {
    switch (action.type) {
        case GET_CARTS:
            return { ...action.carts }
        default:
            return state
    }
}
