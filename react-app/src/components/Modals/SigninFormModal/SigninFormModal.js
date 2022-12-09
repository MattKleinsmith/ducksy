import { useDispatch, useSelector } from 'react-redux';
import { Modal } from '../../../context/Modal';
import { setSigninModal } from '../../../store/ui';
import SigninForm from './SigninForm';

function SigninFormModal() {
    const dispatch = useDispatch();
    const showSigninModal = useSelector(state => state.ui.showSigninModal);
    return showSigninModal ?
        (
            <Modal onClose={() => dispatch(setSigninModal(false))}>
                <SigninForm />
            </Modal>
        ) :
        (
            <div onClick={() => dispatch(setSigninModal(true))}>Sign up</div>
        );
}

export default SigninFormModal;
