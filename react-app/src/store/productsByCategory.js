import { csrfFetch } from './csrf';

const GET_PRODUCTS_BY_CATEGORY = 'products/GET_PRODUCTS_BY_CATEGORY';

export const getProductsByCategory = () => async dispatch => {
    const response = await csrfFetch('/api/products?category=bag&category=gift');
    const products = await response.json();
    dispatch({ type: GET_PRODUCTS_BY_CATEGORY, products });
};

export default function productsByCategoryReducer(state = {}, action) {
    switch (action.type) {
        case GET_PRODUCTS_BY_CATEGORY:
            return action.products.reduce((products, product) => {
                products[product.id] = product;
                return products;
            }, {});
        default:
            return state;
    }
};
