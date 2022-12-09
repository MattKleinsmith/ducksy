import { csrfFetch } from './csrf';

const GET_REVIEWS_BY_PRODUCT_ID = 'reviews/GET_REVIEWS_BY_PRODUCT_ID';
const GET_REVIEWS = 'reviews/GET_REVIEWS';

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

export const postReview = (body, url) => async () => {
    const response = await csrfFetch('/api/reviews', {
        method: "POST",
        body: JSON.stringify(body)
    });
    const review = await response.json();

    await csrfFetch(`/api/reviews/${review.id}/images`, {
        method: "POST",
        body: JSON.stringify({ url, preview: true })
    });

    return review;
};

export const deleteReview = (reviewId) => async () => {
    const response = await csrfFetch('/api/reviews/' + reviewId, { method: "DELETE", });
    return await response.json();
};

export const patchReview = (reviewId, body) => async dispatch => {
    const response = await csrfFetch('/api/reviews/' + reviewId, {
        method: "PATCH",
        body: JSON.stringify(body)
    });
    return await response.json();
};

export default function reviewsReducer(state = {}, action) {
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
};
