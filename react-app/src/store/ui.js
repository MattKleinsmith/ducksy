const SET_REGISTER_MODAL = 'ui/setRegisterModal';
const SET_SIGNIN_MODAL = 'ui/setSigninModal';
const SET_DELETE_PRODUCT_MODAL = 'ui/setProductDeleteModal'

export const setRegisterModal = showRegisterModal => { return { type: SET_REGISTER_MODAL, showRegisterModal } };
export const setSigninModal = showSigninModal => { return { type: SET_SIGNIN_MODAL, showSigninModal } };
export const setDeleteProductModal = showDeleteProductModal => { return { type: SET_DELETE_PRODUCT_MODAL, showDeleteProductModal } };

export default function uiReducer(state = {}, action) {
    switch (action.type) {
        case SET_REGISTER_MODAL:
            return { ...state, showRegisterModal: action.showRegisterModal };
        case SET_SIGNIN_MODAL:
            return { ...state, showSigninModal: action.showSigninModal };
        case SET_DELETE_PRODUCT_MODAL:
            return { ...state, showDeleteProductModal: action.showDeleteProductModal };
        default:
            return state;
    }
};
