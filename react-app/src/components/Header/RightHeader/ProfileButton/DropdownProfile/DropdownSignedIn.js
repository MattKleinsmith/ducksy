import { useDispatch } from 'react-redux';
import { signOut } from '../../../../../store/session';

export default function DropdownSignedIn({ user }) {
    const dispatch = useDispatch();
    return <>
        <div className="dropdownInfo">Hello, {user.display_name}!</div>
        <div className="dropdownInfo">{user.email}</div>
        <div className="dropdownButton bold" onClick={() => dispatch(signOut())}>Sign out</div>
    </>
}
