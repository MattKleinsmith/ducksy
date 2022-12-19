const SET_REGISTER_MODAL = 'ui/setRegisterModal';
const SET_SIGNIN_MODAL = 'ui/setSigninModal';
const SET_DELETE_PRODUCT_MODAL = 'ui/setProductDeleteModal';
const SET_DELETE_REVIEW_MODAL = 'ui/setReviewDeleteModal';
const SET_REVIEW_MODAL = 'ui/setReviewModal';
const SET_DATA_LOADING_MODAL = 'ui/setDataLoadingModal'

export const setRegisterModal = showRegisterModal => { return { type: SET_REGISTER_MODAL, showRegisterModal }; };
export const setSigninModal = showSigninModal => { return { type: SET_SIGNIN_MODAL, showSigninModal }; };
export const setDeleteProductModal = showDeleteProductModal => { return { type: SET_DELETE_PRODUCT_MODAL, showDeleteProductModal }; };
export const setDeleteReviewModal = showDeleteReviewModal => { return { type: SET_DELETE_REVIEW_MODAL, showDeleteReviewModal }; };
export const setReviewModal = showReviewModal => { return { type: SET_REVIEW_MODAL, showReviewModal }; };
export const setDataLoadingModal = showDataLoadingModal => { return { type: SET_DATA_LOADING_MODAL, showDataLoadingModal } }

export default function uiReducer(state = {}, action) {
    switch (action.type) {
        case SET_REGISTER_MODAL:
            return { ...state, showRegisterModal: action.showRegisterModal };
        case SET_SIGNIN_MODAL:
            return { ...state, showSigninModal: action.showSigninModal };
        case SET_DELETE_PRODUCT_MODAL:
            return { ...state, showDeleteProductModal: action.showDeleteProductModal };
        case SET_DELETE_REVIEW_MODAL:
            return { ...state, showDeleteReviewModal: action.showDeleteReviewModal };
        case SET_REVIEW_MODAL:
            return { ...state, showReviewModal: action.showReviewModal };
        case SET_DATA_LOADING_MODAL:
            return { ...state, showDataLoadingModal: action.showDataLoadingModal }
        default:
            return state;
    }
};
