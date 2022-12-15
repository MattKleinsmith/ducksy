import { useNavigate } from "react-router";
import styles from "./CartButton.module.css";

export default function CartButton() {
    const navigate = useNavigate();
    return (
        <>
            <button
                className={styles.cartButton}
                onClick={() => navigate('/cart')}
            >
                <i className="fa-solid fa-cart-shopping" />
            </button>
        </>
    );
}
