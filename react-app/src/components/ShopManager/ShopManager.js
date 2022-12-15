import { useSelector } from 'react-redux';
import ShopManagerItem from "./ShopManagerItem/ShopManagerItem";
import styles from "./ShopManager.module.css";

export default function ShopManager() {
    const user = useSelector(state => state.session.user)

    let products = useSelector(state => Object.values(state.products))
        .filter(product => product.seller_id === user.id);

    products = [{
        preview_image: "/add_a_listing.png"
    }].concat(products);

    const minItems = 10
    if (products.length < minItems) {
        const diff = minItems - products.length;
        for (let i = 0; i < diff; i++) {
            products.push({
                preview_image: "/placeholder.png"
            })
        }
    }

    return (
        <div className={styles.ShopManagerWrapper}>
            <div className={styles.ShopManagerTitle}>
                <h1>Add draft listings to your shop.</h1>
            </div>
            <div className={styles.ShopManager}>
                {products.map((product, i) => <ShopManagerItem product={product} key={i} />)}
            </div>
        </div>
    );
}
