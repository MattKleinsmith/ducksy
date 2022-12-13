import { useSelector } from 'react-redux';
import RegisterFormModal from './RegisterFormModal/RegisterFormModal';
import SigninFormModal from './SigninFormModal/SigninFormModal';
import DeleteProductFormModal from './DeleteProductFormModal/DeleteProductFormModal';
import ReviewFormModal from './ReviewFormModal/ReviewFormModal';
import EditReviewFormModal from './EditReviewFormModal/EditReviewFormModal';


export default function Modals() {
    const ui = useSelector(state => state.ui);
    return <>
        {ui.showRegisterModal && <RegisterFormModal />}
        {ui.showSigninModal && <SigninFormModal />}
        {ui.showDeleteProductModal && <DeleteProductFormModal />}
        {ui.showReviewModal && <ReviewFormModal />}
        {ui.showEditReviewModal && <EditReviewFormModal />}
    </>;
}
