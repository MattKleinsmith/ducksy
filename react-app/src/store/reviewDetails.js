const SET_REVIEW_DETAILS = 'reviewDetails/SET_REVIEW_ID';
const CLEAR_REVIEW_DETAILS = 'reviewDetails/CLEAR_REVIEW_ID';

export const setReviewDetails = (reviewId, review, rating, productId) => {
    return { type: SET_REVIEW_DETAILS, id: reviewId, review, rating, productId };
};

export const clearReviewDetails = () => {
    return { type: CLEAR_REVIEW_DETAILS };
};

export default function ReviewDetailsReducer(state = null, action) {
    switch (action.type) {
        case SET_REVIEW_DETAILS:
            return { id: action.id, review: action.review, rating: action.rating, productId: action.productId };
        case CLEAR_REVIEW_DETAILS:
            return null;
        default:
            return state;
    }
}
