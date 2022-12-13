import { csrfFetch } from './csrf';

const GET_REVIEWS_BY_PRODUCT_ID = 'reviews/GET_REVIEWS_BY_PRODUCT_ID';
const GET_REVIEWS = 'reviews/GET_REVIEWS';
const POST_REVIEW = 'reviews/POST_REVIEW';
const DELETE_REVIEW = 'reviews/DELETE_REVIEW';

export const getReviewsByProductId = (productId) => async dispatch => {
    console.log("getReviewsByProductId");
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

export const postReview = (productId, data) => async dispatch => {
    const response = await csrfFetch(`/api/products/${productId}/reviews`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    });
    if (response.ok) {
        const review = await response.json();
        dispatch({ type: POST_REVIEW, review });
        return response;
    }
};

// export const postReview = (body, url) => async () => {
//     const response = await csrfFetch('/api/reviews', {
//         method: "POST",
//         body: JSON.stringify(body)
//     });
//     const review = await response.json();

//     await csrfFetch(`/api/reviews/${review.id}/images`, {
//         method: "POST",
//         body: JSON.stringify({ url, preview: true })
//     });

//     return review;
// };

export const deleteReview = (reviewId) => async dispatch => {
    const response = await csrfFetch(`/api/reviews/${reviewId}`, { method: "DELETE" });
    if (response.ok)
        dispatch({ type: DELETE_REVIEW, reviewId });
};

export const updateReview = (reviewId, body) => async dispatch => {
    const response = await csrfFetch(`/api/reviews/${reviewId}`, {
        method: "PUT",
        body: JSON.stringify(body)
    });
    return await response.json();
};

export default function reviewsReducer(state = {}, action) {
    let newState = { ...state };
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
        case POST_REVIEW:
            newState[action.review.id] = action.review;
            return newState;
        case DELETE_REVIEW:
            delete newState[action.id];
            return newState;
        default:
            return state;
    }
};
