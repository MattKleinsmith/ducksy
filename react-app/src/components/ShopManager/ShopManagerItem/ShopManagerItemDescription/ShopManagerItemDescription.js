import styles from "./ShopManagerItemDescription.module.css"
export default function ShopManagerItemDescription({ product }) {
    return (
        <div className={styles.ShopManagerItemDescription}>
            <div className={styles.ShopManagerItemDescriptionName}>{product.name}</div>
            {product.price && <div className={styles.priceWrapper}><div className={styles.ShopManagerItemPrice}><strong>${parseFloat(product.price).toFixed(2)}</strong></div></div>}
        </div >
    );
}
