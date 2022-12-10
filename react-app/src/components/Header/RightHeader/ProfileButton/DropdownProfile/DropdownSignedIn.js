import { useDispatch } from 'react-redux';
import { signOut } from '../../../../../store/session';
import { Link } from 'react-router-dom';

export default function DropdownSignedIn({ user }) {
    const dispatch = useDispatch();
    return <>
        <div className="dropdownInfo">Hello, {user.display_name}!</div>
        <div className="dropdownInfo">{user.email}</div>
        <div className="purchases_reviews">
            <Link to="/purchases_reviews">Purhases and reviews</Link>
        </div>
        <div className="dropdownButton bold" onClick={() => dispatch(signOut())}>Sign out</div>
    </>;
}
