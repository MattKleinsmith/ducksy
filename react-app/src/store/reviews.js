import { csrfFetch } from './csrf';

const GET_REVIEWS_BY_PRODUCT_ID = 'reviews/GET_REVIEWS_BY_PRODUCT_ID';
const GET_REVIEWS_BY_BUYER_ID = 'reviews/GET_REVIEWS_BY_BUYER_ID';
const GET_REVIEWS = 'reviews/GET_REVIEWS';
const POST_REVIEW = 'reviews/POST_REVIEW';
const UPDATE_REVIEW = ' reviews/UPDATE_REVIEW';
const DELETE_REVIEW = 'reviews/DELETE_REVIEW';

export const getReviewsByProductId = (productId) => async dispatch => {
    console.log("getReviewsByProductId");
    const response = await csrfFetch(`/api/products/${productId}/reviews`);

    const reviews = await response.json();
    dispatch({ type: GET_REVIEWS_BY_PRODUCT_ID, reviews });
    return response;
};

export const getReviewsByBuyerId = () => async dispatch => {
    const response = await csrfFetch(`/api/users/reviews`);

    const reviews = await response.json();
    dispatch({ type: GET_REVIEWS_BY_BUYER_ID, reviews });
    return response;
};

export const getReviews = () => async dispatch => {
    const response = await csrfFetch('/api/reviews');

    const reviews = await response.json();
    dispatch({ type: GET_REVIEWS, reviews });
    return response;
};

export const postReview = (productId, data) => async dispatch => {
    const response = await csrfFetch(`/api/products/${productId}/reviews`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    });
    if (response.ok) {
        const review = await response.json();
        dispatch({ type: POST_REVIEW, review });
        return review;
    }
};

export const deleteReview = (reviewId) => async dispatch => {
    const response = await csrfFetch(`/api/reviews/${reviewId}`, { method: "DELETE" });
    if (response.ok) {
        dispatch({ type: DELETE_REVIEW, reviewId });
        return await response.json();
    };
};

export const updateReview = (reviewId, body) => async dispatch => {
    const response = await csrfFetch(`/api/reviews/${reviewId}`, {
        method: "PUT",
        body: JSON.stringify(body)
    });
    if (response.ok) {
        const review = await response.json();
        dispatch({ type: UPDATE_REVIEW, review });
        return review;
    }
};

export default function reviewsReducer(state = {}, action) {
    let newState = { ...state };
    switch (action.type) {
        case GET_REVIEWS_BY_PRODUCT_ID:
            return action.reviews.reduce((reviews, review) => {
                reviews[review.id] = review;
                return reviews;
            }, {});
        case GET_REVIEWS_BY_BUYER_ID:
            return action.reviews.reduce((reviews, review) => {
                reviews[review.product_id] = review;
                return reviews;
            }, {});
        case GET_REVIEWS:
            return action.reviews.reduce((reviews, review) => {
                reviews[review.id] = review;
                return reviews;
            }, {});
        case POST_REVIEW:
            newState[action.review.id] = action.review;
            return newState;
        case UPDATE_REVIEW:
            newState[action.review.id] = action.review;
            return newState;
        case DELETE_REVIEW:
            delete newState[action.reviewId];
            return newState;
        default:
            return state;
    }
};
