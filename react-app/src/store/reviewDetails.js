
const SET_REVIEW_DETAILS = 'reviewDetails/SET_REVIEW_ID';

export const setReviewId = (reviewId, review, rating) => {
    return { type: SET_REVIEW_DETAILS, id: reviewId, review: review, rating: rating };
};

export default function ReviewDetailsReducer(state = {}, action) {
    switch (action.type) {
        case SET_REVIEW_DETAILS:
            return { id: action.id, review: action.review, rating: action.rating };
        default:
            return state;
    }
}
