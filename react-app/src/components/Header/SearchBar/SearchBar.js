import styles from "./SearchBar.module.css";
import { useState, useEffect } from "react";
import { useDispatch } from "react-redux";
import { getProductsByCategory } from "../../../store/productsByCategory";

export default function SearchBar() {
    const [isSearchBarActive, setIsSearchBarActive] = useState(false);
    const dispatch = useDispatch();

    useEffect(() => {
        if (!isSearchBarActive) return;
        const setSearchBarInactive = e => {
            setIsSearchBarActive(false);
        }
        document.addEventListener('click', setSearchBarInactive);
        return () => document.removeEventListener("click", setSearchBarInactive);
    }, [isSearchBarActive]);

    const handleSearch = () => {
        dispatch(getProductsByCategory())
    }

    return (
        <div className={styles.searchBarWrapper} onClick={() => setIsSearchBarActive(true)}>
            <input type="text" className={styles.searchBar} placeholder="Search for anything" />
            <div onClick={handleSearch} className={`${styles.iconWrapperBase} ${isSearchBarActive && styles.iconWrapperActive}`}>
                <i className={`fa-solid fa-magnifying-glass ${isSearchBarActive ? styles.iconActive : styles.icon}`} />
            </div>
        </div>
    )
}
