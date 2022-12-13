import { useDispatch } from 'react-redux';
import { Link, useNavigate } from 'react-router-dom';
import { signOut } from '../../../../../store/session';

export default function DropdownSignedIn({ user }) {
    const dispatch = useDispatch();
    const navigate = useNavigate();

    const onClickSignOut = () => {
        dispatch(signOut());
        navigate("/");
    }
    return <>
        <div className="dropdownInfo">Hello, {user.display_name}!</div>
        <div className="dropdownInfo">{user.email}</div>
        <div>
            <Link to='/your/purchases'>Purchases and Reviews</Link>
        </div>
        <div className="dropdownButton bold" onClick={onClickSignOut}>Sign out</div>
    </>;
}
