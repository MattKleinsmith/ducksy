import { csrfFetch } from './csrf';

const GET_REVIEWS_BY_PRODUCT_ID = 'productReviews/GET_REVIEWS_BY_PRODUCT_ID';
const GET_REVIEWS = 'productReviews/GET_REVIEWS';

export const getReviewsByProductId = (productId) => async dispatch => {
    const response = await csrfFetch(`/api/products/${productId}/reviews`);

    const reviews = await response.json();
    dispatch({ type: GET_REVIEWS_BY_PRODUCT_ID, reviews });
    return response;
};

export const getReviews = () => async dispatch => {
    const response = await csrfFetch('/api/reviews');

    const reviews = await response.json();
    dispatch({ type: GET_REVIEWS, reviews });
    return response;
};

export default function productReviewsReducer(state = {}, action) {
    switch (action.type) {
        case GET_REVIEWS_BY_PRODUCT_ID:
            return action.reviews.reduce((reviews, review) => {
                reviews[review.id] = review;
                return reviews;
            }, {});
        case GET_REVIEWS:
            return action.reviews.reduce((reviews, review) => {
                reviews[review.id] = review;
                return reviews;
            }, {});
        default:
            return state;
    }
}
