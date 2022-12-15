const SET_PRODUCT_ID = 'productDetails/SET_PRODUCT_ID';

export const setProductId = productId => {
    return { type: SET_PRODUCT_ID, id: productId }
}

export default function productDetailsReducer(state = {}, action) {
    switch (action.type) {
        case SET_PRODUCT_ID:
            return { id: action.id };
        default:
            return state;
    }
};
