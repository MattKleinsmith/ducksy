const SET_STATE = 'productEditor/SET_STATE';

export const setProductEditorState = state => {
    return { type: SET_STATE, state }
}

export default function productDetailsReducer(state = {}, action) {
    switch (action.type) {
        case SET_STATE:
            return { ...state, ...action.state };
        default:
            return state;
    }
};
