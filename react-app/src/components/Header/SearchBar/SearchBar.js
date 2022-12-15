import styles from "./SearchBar.module.css";
import { useDispatch, useSelector } from "react-redux";
import { setSigninModal } from "../../../store/ui";

export default function SearchBar() {
    const session = useSelector(state => state.session);
    const dispatch = useDispatch();
    return (
        <input type="text" className={styles.searchBar} placeholder="Search for anything" />
    )
}
