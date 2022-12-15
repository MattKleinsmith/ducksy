import styles from "./SearchBar.module.css";
import { useDispatch, useSelector } from "react-redux";
import { setSigninModal } from "../../../store/ui";

export default function SearchBar() {
    const session = useSelector(state => state.session);
    const dispatch = useDispatch();
    return (
        <div className={styles.searchBarWrapper}>
            <input type="text" className={styles.searchBar} placeholder="Search for anything" />
            <div className={styles.iconWrapper}>
                <i className={`fa-solid fa-magnifying-glass ${styles.icon}`} />
            </div>
        </div>
    )
}
