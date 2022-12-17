import styles from "./ProfileDropdown.module.css";
import { useDispatch } from 'react-redux';
import { Link, useNavigate } from 'react-router-dom';
import { signOut } from '../../../../../store/session';

export default function ProfileDropdown({ user, ui }) {
    const dispatch = useDispatch();
    const navigate = useNavigate();

    const onClickSignOut = () => {
        dispatch(signOut());
        if (window.location.href.includes("your"))
            navigate("/");
    };

    return <>
        <div className={styles.wrapper}>

            <div className={styles.row}>
                <div className={`${styles.iconWrapper}`}>
                    <i className={`fas fa-user-circle ${styles.profilePicture}`} />
                </div>
                <div className={styles.right}>
                    <div>{user.display_name}</div>
                    <div>{user.email}</div>
                </div>
            </div>

            <Link className={`${styles.row} ${styles.link}`} to='/your/purchases'>
                <div className={styles.iconWrapper}><i className={`fa-regular fa-clipboard`} /></div>
                <div className={`${styles.right} ${styles.purchases}`}>
                    Purchases
                </div>
            </Link>

            <div className={`${styles.row} ${styles.signOut}`} onClick={onClickSignOut}>
                <div className={styles.iconWrapper}>
                    <i className={`fa-solid fa-arrow-right-from-bracket`} />
                </div>
                <div className={`${styles.right}`}>Sign out</div>
            </div>

        </div>
    </>;
}
