import { useDispatch, useSelector } from 'react-redux';
import { Modal } from '../../../context/Modal';
import { setRegisterModal } from '../../../store/ui';
import RegisterForm from './RegisterForm';

function RegisterFormModal() {
    const dispatch = useDispatch();
    const showRegisterModal = useSelector(state => state.ui.showRegisterModal);
    return showRegisterModal ?
        (
            <Modal onClose={() => dispatch(setRegisterModal(false))}>
                <RegisterForm />
            </Modal>
        ) :
        (
            <div onClick={() => dispatch(setRegisterModal(true))}>Sign up</div>
        );
}

export default RegisterFormModal;
