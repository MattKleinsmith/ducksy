import { useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { addItemToCart } from "../../../../../store/shoppingCart";
import styles from './BuyItAgain.module.css';

export default function BuyItAgain({ product }) {
    const dispatch = useDispatch();
    const user = useSelector(state => state.session.user);
    const [hasAddedToCart, setHasAddedToCart] = useState(false);
    return (
        <div>
            <div className={styles.buyAgain}>
                <div><button
                    onClick={() => {
                        setHasAddedToCart(true)
                        dispatch(addItemToCart(product, user))
                    }}
                    className={styles.buyAgainBtn}>Buy this again</button>
                </div>
                <div className={styles.price}>{`$${parseFloat(product.price).toFixed(2)}`}</div>
            </div>
            {hasAddedToCart && <div className={styles.addedToCart}>Added to cart!</div>}
        </div>
    )
}
