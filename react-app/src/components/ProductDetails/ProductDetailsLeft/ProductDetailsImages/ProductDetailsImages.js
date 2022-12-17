import styles from "./ProductDetailsImages.module.css";

export default function ProductDetailsImages({ product }) {
    
    return (
        <div className={styles.ProductDetailsImagesWrapper}>
                <div className={styles.moreImagesWrapper}>
                    {product.product_images.map(img =>
                        <img src={img.url} alt="ProductDetailsImages" className={styles.moreImages} />)}
                </div>
                <div className={styles.defaultImageWrapper}>
                    <img src={product.preview_image} alt="ProductDetailsImages" className={styles.defaultImage} />
                </div>
        </div>
    );
}
