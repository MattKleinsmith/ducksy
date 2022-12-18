import styles from "./ProductDetailsImages.module.css";
import { useState } from "react";

export default function ProductDetailsImages({ product }) {
    const [url, setUrl] = useState(product.preview_image);

    const onClickHandler = (productImageId) => {
        const image = product.product_images.find(image => image.id === productImageId);
        setUrl(image.url);
    };

    return (
        <div className={styles.ProductDetailsImagesWrapper}>
            <div type='checkbox' className={styles.moreImagesWrapper}>
                {product.product_images.map(product_image =>
                    <button className={styles.moreImagesBtn} onClick={() => onClickHandler(product_image.id)} key={product_image.id}>
                        <img src={product_image.url} alt="ProductDetailsImages" className={styles.moreImages} />
                    </button>)}
            </div>
            <div className={styles.defaultImageWrapper}>
                <img src={url} alt="ProductDetailsImages" className={styles.defaultImage} />
            </div>
        </div >
    );
}
