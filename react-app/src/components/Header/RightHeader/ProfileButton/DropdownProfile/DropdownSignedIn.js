import { useDispatch } from 'react-redux';
import { Link, useNavigate } from 'react-router-dom';
import { signOut } from '../../../../../store/session';
import styles from "./DropdownProfile.module.css";

export default function DropdownSignedIn({ user }) {
    const dispatch = useDispatch();
    const navigate = useNavigate();

    const onClickSignOut = () => {
        dispatch(signOut());
        if (window.location.href.includes("your"))
            navigate("/");
    };
    return <>
        <div className={styles.iconInfoWrapper}>
            <span className={styles.icon} style={{ color: 'rgb(110, 110, 110)' }}><i className="fas fa-user-circle" /></span>
            <div>
                <div className={styles.dropdownInfo}>{user.display_name}</div>
                <div className={styles.dropdownInfo}>{user.email}</div>
            </div>
        </div>
        <div className={styles.iconInfoWrapper}>
            <span className={styles.icon}><i className="fa-regular fa-clipboard"></i></span>
            <div className={styles.dropdownLink}><Link to='/your/purchases' className={styles.dropdownLink}>Purchases</Link></div>
        </div>
        <div className={styles.iconInfoWrapper}>
            <span className={styles.icon}><i className="fa-solid fa-arrow-right-from-bracket"></i></span>
            <div className={styles.dropdownBtn} onClick={onClickSignOut}>Sign out</div>
        </div>
    </>;
}
