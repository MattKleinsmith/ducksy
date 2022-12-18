import styles from "./HomepageItem.module.css";

export default function HomepageItem({ product }) {

    return (
        // <div className={styles.itemWrapper}>
        <div className={styles.item}>
            <img src={product.preview_image} alt={product.preview_image} onError={(e) => { e.target.src = "/images/placeholder.png"; }} />
        </div>

        // </div>
    );
}
