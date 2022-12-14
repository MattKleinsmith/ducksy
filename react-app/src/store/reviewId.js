import { csrfFetch } from './csrf';

const SET_REVIEW_ID = 'reviewId/SET_REVIEW_ID';

export const setReviewId = (reviewId) => {
    return { type: SET_REVIEW_ID, id: reviewId };
};

export default function ReviewIdReducer(state = {}, action) {
    switch (action.type) {
        case SET_REVIEW_ID:
            return { id: action.id };
        default:
            return state;
    }
}
