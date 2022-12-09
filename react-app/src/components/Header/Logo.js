import { Link } from 'react-router-dom';

export default function Logo() {
    return (
        <Link exact="true" to="/" style={{ textDecoration: 'none' }}>
            <span id="logo">Ducksy</span>
        </Link>
    )
}
