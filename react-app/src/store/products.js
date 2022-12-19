import { csrfFetch } from './csrf';

const GET_PRODUCT = 'products/GET_INDIVIUDAL_PRODUCT';
const GET_PRODUCTS = 'products/GET_PRODUCTS';
const ADD_PRODUCT = 'products/ADD_PRODUCT';
const ADD_IMAGE = 'products/ADD_IMAGE';
const DELETE_PRODUCT = 'products/DELETE_PRODUCT';

export const getProducts = () => async dispatch => {
    const response = await csrfFetch('/api/products');
    const products = await response.json();
    dispatch({ type: GET_PRODUCTS, products });
};

export const getProduct = (productId) => async dispatch => {
    const response = await csrfFetch(`/api/products/${productId}`);
    const product = await response.json();
    dispatch({ type: GET_PRODUCT, product });
};

export const postProduct = body => async dispatch => {
    const response = await csrfFetch('/api/products', {
        method: "POST",
        body: JSON.stringify(body)
    });
    const product = await response.json();
    dispatch({ type: ADD_PRODUCT, product });
    return product.id;
};

export const putProduct = (productId, body) => async dispatch => {
    await csrfFetch(`/api/products/${productId}`, {
        method: "PUT",
        body: JSON.stringify(body)
    });
    dispatch(getProduct(productId));
};

export const postProductImage = (productId, image, preview) => async dispatch => {
    const formData = new FormData();

    formData.append('image', image);
    formData.append('preview', preview);

    const response = await fetch(`/api/products/${productId}/images`, {
        method: "POST",
        body: formData
    });

    if (response.status >= 400) {
        const errors = await response.json();
        console.log(errors);
        throw errors;
    }

    const product_image = await response.json();

    dispatch({ type: ADD_IMAGE, productId, product_image })
};

export const deleteProduct = productId => async dispatch => {
    await csrfFetch(`/api/products/${productId}`, { method: "DELETE" });
    dispatch({ type: DELETE_PRODUCT, productId });
};

export default function productsReducer(state = {}, action) {
    const newState = { ...state };
    switch (action.type) {
        case GET_PRODUCTS:
            return action.products.reduce((products, product) => {
                products[product.id] = product;
                return products;
            }, {});
        case ADD_PRODUCT:
            newState[action.product.id] = action.product;
            return newState;
        case GET_PRODUCT:
            newState[action.product.id] = action.product;
            return newState;
        case ADD_IMAGE:
            newState[action.productId].preview_image = action.product_image.url;
            newState[action.productId].product_images.push(action.product_image);
            return newState;
        case DELETE_PRODUCT:
            delete newState[action.productId];
            return newState;
        default:
            return state;
    }
};
