import { csrfFetch } from './csrf';
import { getProduct } from './products';

const GET_REVIEWS_BY_BUYER_ID = 'buyerReviews/GET_REVIEWS_BY_BUYER_ID';
const POST_REVIEW = 'buyerReviews/POST_REVIEW';
const UPDATE_REVIEW = ' buyerReviews/UPDATE_REVIEW';
const DELETE_REVIEW = 'buyerReviews/DELETE_REVIEW';


export const getReviewsByBuyerId = () => async dispatch => {
    const response = await csrfFetch(`/api/reviews/current`);
    const reviews = await response.json();
    dispatch({ type: GET_REVIEWS_BY_BUYER_ID, reviews });
    return response;
};

export const postReview = (productId, data) => async dispatch => {
    const response = await csrfFetch(`/api/products/${productId}/reviews`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    });
    const review = await response.json();
    dispatch({ type: POST_REVIEW, review });
    await dispatch(getProduct(productId));
};

export const deleteReview = (review) => async dispatch => {
    await csrfFetch(`/api/reviews/${review.id}`, { method: "DELETE" });
    await dispatch({ type: DELETE_REVIEW, review });
    dispatch(getReviewsByBuyerId());
    console.log("deleteReview", review, review.productId);
    await dispatch(getProduct(review.productId));
};

export const updateReview = (oldReview, body) => async dispatch => {
    const response = await csrfFetch(`/api/reviews/${oldReview.id}`, {
        method: "PUT",
        body: JSON.stringify(body)
    });
    const review = await response.json();
    dispatch({ type: UPDATE_REVIEW, review });
    await dispatch(getProduct(review.product_id));
};

export default function buyerReviewsReducer(state = {}, action) {
    let newState = { ...state };
    switch (action.type) {
        case GET_REVIEWS_BY_BUYER_ID:
            return action.reviews.reduce((reviews, review) => {
                reviews[review.product_id] = review;
                return reviews;
            }, {});
        case POST_REVIEW:
            newState[action.review.product_id] = action.review;
            return newState;
        case UPDATE_REVIEW:
            newState[action.review.product_id] = action.review;
            return newState;
        case DELETE_REVIEW:
            delete newState[action.review.product_id];
            return newState;
        default:
            return state;
    }
};
