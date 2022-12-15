import { useDispatch } from 'react-redux';
import { Link } from 'react-router-dom';
import { clearSearch } from '../../store/productsBySearch';
import { clearSearchQuery } from '../../store/searchQuery';
import styles from "./Header.module.css"

export default function Logo() {
    const dispatch = useDispatch();

    const handleClick = () => {
        dispatch(clearSearch());
        dispatch(clearSearchQuery());
    }

    return (
        <div>
            <Link to="/" style={{ textDecoration: 'none' }}>
                <span onClick={handleClick} exact="true" className={styles.logo}>Ducksy</span>
            </Link>
        </div>
    )
}
