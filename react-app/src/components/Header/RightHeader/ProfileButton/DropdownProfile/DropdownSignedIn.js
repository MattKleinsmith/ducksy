import { useDispatch } from 'react-redux';
import { Link } from 'react-router-dom';
import { signOut } from '../../../../../store/session';

export default function DropdownSignedIn({ user }) {
    const dispatch = useDispatch();
    return <>
        <div className="dropdownInfo">Hello, {user.display_name}!</div>
        <div className="dropdownInfo">{user.email}</div>
        <div>
            <Link to='/purchases_reviews'>Purchases and Reviews</Link>
        </div>
        <div className="dropdownButton bold" onClick={() => dispatch(signOut())}>Sign out</div>
    </>;
}
