import styles from "./SearchBar.module.css";
import { useState, useEffect, useRef } from "react";
import { useDispatch } from "react-redux";
import { getProductsByKeywords } from "../../../store/productsBySearch";

export default function SearchBar() {
    const [isSearchBarActive, setIsSearchBarActive] = useState(false);
    const [search, setSearch] = useState("");
    const dispatch = useDispatch();
    const searchBar = useRef(null);

    useEffect(() => {
        if (!isSearchBarActive) return;
        const setSearchBarInactive = e => {
            if (e.target === searchBar.current || search) return;
            setIsSearchBarActive(false);
        }
        document.addEventListener('click', setSearchBarInactive);
        return () => document.removeEventListener("click", setSearchBarInactive);
    }, [isSearchBarActive, search]);

    const handleSearchBarClick = () => {
        setIsSearchBarActive(true);
    }

    const handleSearch = (e) => {
        if (e) e.preventDefault();
        dispatch(getProductsByKeywords(search.split(" ")));
    }

    const onSearchChange = e => {
        setSearch(e.target.value)
    }

    return (
        <div className={styles.wrapper}>
            <div className={styles.searchBarWrapper} onClick={handleSearchBarClick}>
                <form onSubmit={handleSearch} className={styles.form}>
                    <input
                        type="text"
                        ref={searchBar}
                        className={styles.searchBar}
                        value={search}
                        onChange={onSearchChange}
                        placeholder="Search for anything" />
                </form>
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
