import { useNavigate } from "react-router";
import styles from "./ShopButton.module.css";

export default function ShopButton() {
    const navigate = useNavigate();
    return (
        <>
            <button className={styles.shopButton} onClick={() => navigate("/your/shop")}>
                <i className="fa-solid fa-shop" />
            </button>
        </>
    );
}
