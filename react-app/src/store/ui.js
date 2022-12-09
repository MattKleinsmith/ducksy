const SET_REGISTER_MODAL = 'ui/setRegisterModal';
const SET_SIGNIN_MODAL = 'ui/setSigninModal';

export const setRegisterModal = showRegisterModal => { return { type: SET_REGISTER_MODAL, showRegisterModal } };
export const setSigninModal = showSigninModal => { return { type: SET_SIGNIN_MODAL, showSigninModal } };

export default function uiReducer(state = {}, action) {
    switch (action.type) {
        case SET_REGISTER_MODAL:
            return { ...state, showRegisterModal: action.showRegisterModal };
        case SET_SIGNIN_MODAL:
            return { ...state, showSigninModal: action.showSigninModal };
        default:
            return state;
    }
};
