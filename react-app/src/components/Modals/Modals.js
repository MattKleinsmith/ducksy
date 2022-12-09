import { useSelector } from 'react-redux';
import RegisterFormModal from './RegisterFormModal/RegisterFormModal';
import SigninFormModal from './SigninFormModal/SigninFormModal';

export default function Modals() {
    const ui = useSelector(state => state.ui);
    return <>
        {ui.showRegisterModal && <RegisterFormModal />}
        {ui.showSigninModal && <SigninFormModal />}
    </>
}
