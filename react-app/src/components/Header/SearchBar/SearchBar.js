import styles from "./SearchBar.module.css";
import { useState, useEffect, useRef } from "react";
import { useDispatch } from "react-redux";
import { getProductsByCategory } from "../../../store/productsByCategory";

export default function SearchBar() {
    const [isSearchBarActive, setIsSearchBarActive] = useState(false);
    const dispatch = useDispatch();
    const searchBar = useRef(null);

    useEffect(() => {
        if (!isSearchBarActive) return;
        const setSearchBarInactive = e => {
            console.log(e.target);
            if (e.target == searchBar.current) return;
            setIsSearchBarActive(false);
        }
        document.addEventListener('click', setSearchBarInactive);
        return () => document.removeEventListener("click", setSearchBarInactive);
    }, [isSearchBarActive]);

    const handleSearchBarClick = () => {
        setIsSearchBarActive(true);
    }

    const handleSearch = () => {
        dispatch(getProductsByCategory())
    }

    return (
        <div className={styles.wrapper}>
            <div className={styles.searchBarWrapper} onClick={handleSearchBarClick}>
                <input type="text" ref={searchBar} className={styles.searchBar} placeholder="Search for anything" />
                <div onClick={handleSearch} className={`${styles.iconWrapperBase} ${isSearchBarActive && styles.iconWrapperActive}`}>
                    <i className={`fa-solid fa-magnifying-glass ${isSearchBarActive ? styles.iconActive : styles.icon}`} />
                </div>
            </div>
            {false && isSearchBarActive && <div>
                <br />
                <div>We can show recently viewed items here.</div>
                <div>And if they have no recently viewed items, we can show some categories.</div>
                <div>The categories that we show can be different than the ones we show on the homepage.</div>
            </div>}
        </div >
    )
}
