import styles from "./SearchBar.module.css";
import { useState, useEffect, useRef } from "react";
import { useDispatch, useSelector } from "react-redux";
import { getProductsByKeywords } from "../../../store/productsBySearch";
import { setSearchQuery } from "../../../store/searchQuery";
import { useNavigate } from "react-router";

export default function SearchBar() {
    const [isSearchBarActive, setIsSearchBarActive] = useState(false);
    const searchQuery = useSelector(state => state.searchQuery);
    const dispatch = useDispatch();
    const searchBar = useRef(null);
    const navigate = useNavigate();

    useEffect(() => {
        if (!isSearchBarActive) return;
        const setSearchBarInactive = e => {
            if (e.target === searchBar.current || searchQuery) return;
            setIsSearchBarActive(false);
        }
        document.addEventListener('click', setSearchBarInactive);
        return () => document.removeEventListener("click", setSearchBarInactive);
    }, [isSearchBarActive, searchQuery]);

    const handleSearchBarClick = () => {
        setIsSearchBarActive(true);
    }

    const onSearchChange = e => {
        dispatch(setSearchQuery(e.target.value))
    }

    const handleSearch = async (e) => {
        if (e) e.preventDefault();
        await dispatch(getProductsByKeywords(searchQuery.split(" ")));
        navigate("/listings");
    }

    return (
        <div className={styles.wrapper}>
            <div className={styles.searchBarWrapper} onClick={handleSearchBarClick}>
                <form onSubmit={handleSearch} className={styles.form}>
                    <input
                        type="text"
                        ref={searchBar}
                        className={styles.searchBar}
                        value={searchQuery}
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
