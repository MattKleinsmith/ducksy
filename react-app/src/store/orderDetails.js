import { csrfFetch } from "./csrf";

const GET_ORDER_DETAILS = 'order_details/GET_ORDER_DETAILS';

export const getCurrentUserOrders = () => async dispatch => {
    const response = await csrfFetch(`/api/order_details/current`);
    const order_details = await response.json();
    dispatch({ type: GET_ORDER_DETAILS, order_details });
    return order_details;
};

export default function orderDetailsReducer(state = {}, action) {
    switch (action.type) {
        case GET_ORDER_DETAILS:
            const newState = { ...state, ...action.order_details };
            return newState;
        default:
            return state;
    }
}
