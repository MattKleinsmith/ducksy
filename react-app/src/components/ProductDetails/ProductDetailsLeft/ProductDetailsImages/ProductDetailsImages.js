import styles from "./ProductDetailsImages.module.css";

export default function ProductDetailsImages({ product }) {
    return (
        <div className={styles.ProductDetailsImagesWrapper}>
            <div className={styles.ProductDetailsImages}>
                <img src={product.preview_image} alt="ProductDetailsImages" />
            </div>
        </div>
    );
}
