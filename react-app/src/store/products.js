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

export const postProductImage = (productId, image, preview) => async dispatch => {
    const formData = new FormData();

    formData.append('image', image);
    formData.append('preview', preview);

    const response = await fetch(`/api/products/${productId}/images`, {
        method: "POST",
        body: formData
    });

    await response.json();
    dispatch(getProducts())
};

export const deleteProduct = productId => async dispatch => {
    console.log("deleteProduct", productId);
    const response = await csrfFetch('/api/products/' + productId, { method: "DELETE", });
    await response.json();
    dispatch(getProducts());
};

export const putProduct = (productId, body) => async dispatch => {
    const response = await csrfFetch('/api/products/' + productId, {
        method: "PUT",
        body: JSON.stringify(body)
    });
    await response.json();
    dispatch(getProducts());
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
