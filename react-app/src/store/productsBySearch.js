import { csrfFetch } from './csrf';

const GET_PRODUCTS_BY_SEARCH = 'productsBySearch/GET_PRODUCTS_BY_SEARCH';
const CLEAR_SEARCH = 'productsBySearch/CLEAR_SEARCH';

export const getProductsByCategory = categories => async dispatch => {
    const response = await csrfFetch(`/api/products?category=${categories.join("&category=")}`);
    const products = await response.json();
    dispatch({ type: GET_PRODUCTS_BY_SEARCH, products });
};

export const getProductsByKeywords = keywords => async dispatch => {
    const response = await csrfFetch(`/api/products?q=${keywords.join("&q=")}`);
    const products = await response.json();
    dispatch({ type: GET_PRODUCTS_BY_SEARCH, products });
};

export const clearSearch = () => {
    return { type: CLEAR_SEARCH }
}

export default function productsBySearchReducer(state = {}, action) {
    switch (action.type) {
        case GET_PRODUCTS_BY_SEARCH:
            return action.products.reduce((products, product) => {
                products[product.id] = product;
                return products;
            }, {});
        case CLEAR_SEARCH:
            return {};
        default:
            return state;
    }
};
