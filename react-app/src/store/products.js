import { csrfFetch } from './csrf';

const GET_PRODUCTS = 'products/GET_PRODUCTS';

export const getProducts = () => async dispatch => {
    const response = await csrfFetch('/api/products');

    const products = await response.json();
    dispatch({ type: GET_PRODUCTS, products });
    return response;
};

export const postProduct = (body, url) => async () => {
    const response = await csrfFetch('/api/products', {
        method: "POST",
        body: JSON.stringify(body)
    });
    const product = await response.json();

    await csrfFetch(`/api/products/${product.id}/images`, {
        method: "POST",
        body: JSON.stringify({ url, preview: true })
    });

    return product;
};

export const deleteProduct = (productId) => async () => {
    const response = await csrfFetch('/api/products/' + productId, { method: "DELETE", });
    return await response.json();
};

export const patchProduct = (productId, body) => async dispatch => {
    const response = await csrfFetch('/api/products/' + productId, {
        method: "PATCH",
        body: JSON.stringify(body)
    });
    return await response.json();
};

export default function productsReducer(state = {}, action) {
    switch (action.type) {
        case GET_PRODUCTS:
            return action.products.reduce((products, product) => {
                products[product.id] = product;
                return products;
            }, {});
        default:
            return state;
    }
};