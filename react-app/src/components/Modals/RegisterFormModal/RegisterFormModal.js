import { useDispatch } from 'react-redux';
import { Modal } from '../../../context/Modal';
import { setRegisterModal } from '../../../store/ui';
import RegisterForm from './RegisterForm';

export default function RegisterFormModal() {
    const dispatch = useDispatch();
    return (
        <Modal onClose={() => dispatch(setRegisterModal(false))}>
            <RegisterForm />
        </Modal>
    );
}
