import { csrfFetch } from "./csrf";

const GET_ORDERS = 'orders/GET_ORDERS';

export const getCurrentUserOrders = () => async dispatch => {
    const response = await csrfFetch(`/api/orders`);
    const orders = await response.json();
    dispatch({ type: GET_ORDERS, orders });
};

export default function ordersReducer(state = {}, action) {
    switch (action.type) {
        case GET_ORDERS:
            let newState = { ...state };
            let ordersArray = action.orders;
            ordersArray.forEach(order => newState[order.id] = order);
            return newState;
        default:
            return state;
    }
}
