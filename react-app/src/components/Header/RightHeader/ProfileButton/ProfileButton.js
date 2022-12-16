import { useState, useEffect } from "react";
import { useSelector } from 'react-redux';

import styles from "./ProfileButton.module.css";
import DropdownProfile from "./DropdownProfile/DropdownProfile";

export default function ProfileButton() {
    const [showMenu, setShowMenu] = useState(false);
    const ui = useSelector(state => state.ui);
    const user = useSelector(state => state.session.user);

    useEffect(() => {
        if (!showMenu) return;
        const closeMenu = () => setShowMenu(false);
        document.addEventListener('click', closeMenu);
        return () => document.removeEventListener("click", closeMenu);
    }, [showMenu]);

    return (
        <>
            <button className={styles.profileButton} onClick={() => setShowMenu(true)}>
                <i className="fas fa-user-circle" />
                <span className={styles.arrow} >▼</span>
            </button>
            {showMenu && <DropdownProfile user={user} ui={ui} />}
        </>
    );
}
