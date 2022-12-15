import styles from "./SearchBar.module.css";
import { useState, useEffect } from "react";

export default function SearchBar() {
    const [isSearchBarActive, setIsSearchBarActive] = useState(false);
    console.log("isSearchBarActive", isSearchBarActive);

    useEffect(() => {
        if (!isSearchBarActive) return;
        const setSearchBarInactive = e => {
            setIsSearchBarActive(false);
        }
        document.addEventListener('click', setSearchBarInactive);
        return () => document.removeEventListener("click", setSearchBarInactive);
    }, [isSearchBarActive]);

    return (
        <div className={styles.searchBarWrapper} onClick={() => setIsSearchBarActive(true)}>
            <input type="text" className={styles.searchBar} placeholder="Search for anything" />
            <div className={`${styles.iconWrapperBase} ${isSearchBarActive && styles.iconWrapperActive}`}>
                <i className={`fa-solid fa-magnifying-glass ${isSearchBarActive ? styles.iconActive : styles.icon}`} />
            </div>
        </div>
    )
}
