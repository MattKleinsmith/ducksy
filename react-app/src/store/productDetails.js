const SET_PRODUCT_ID = 'productDetails/SET_PRODUCT_ID';
// const SET_PRODUCT_URL = 'productDetails/SET_PRODUCT_URL';

export const setProductId = productId => {
    return { type: SET_PRODUCT_ID, id: productId };
};

// export const setProductUrl = (productId, url) => {
//     return { type: SET_PRODUCT_URL, id: productId, url: url };
// };


export default function productDetailsReducer(state = {}, action) {
    switch (action.type) {
        case SET_PRODUCT_ID:
            return { id: action.id };
        // case SET_PRODUCT_URL:
        //     return;
        default:
            return state;
    }
};
