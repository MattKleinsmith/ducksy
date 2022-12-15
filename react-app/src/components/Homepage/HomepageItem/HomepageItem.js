import styles from "./HomepageItem.module.css";

export default function HomepageItem({ product }) {

    return (
        <div>
            <div className={styles.item}>
                <img src={product.preview_image} alt={product.preview_image} onError={(e) => { e.target.src = "/placeholder.png"; }} />
            </div>

        </div>
    );
}
