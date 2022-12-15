import { useDispatch } from 'react-redux';
import { Modal } from '../../../context/Modal';
import { setSigninModal } from '../../../store/ui';
import SigninForm from './SigninForm';

export default function SigninFormModal() {
    const dispatch = useDispatch();
    return (
        <Modal onClose={() => dispatch(setSigninModal(false))}>
            <SigninForm />
        </Modal>
    );
}
