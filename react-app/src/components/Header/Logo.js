import { Link } from 'react-router-dom';
import styles from "./Header.module.css"

export default function Logo() {
    return (
        <div>
            <Link exact="true" to="/" style={{ textDecoration: 'none' }}>
                <span className={styles.logo}>Ducksy</span>
            </Link>
        </div>
    )
}
