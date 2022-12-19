import { useEffect, useState } from "react";
import { useDispatch } from "react-redux";
import { updateItemQuantity } from "../../../../../store/shoppingCart";
import styles from './ItemQuantity.module.css'


export default function ItemQuantity({ initialQuantity, user, product }) {
    const dispatch = useDispatch();
    const [quantity, setQuantity] = useState(initialQuantity);
    useEffect(() => {
        dispatch(updateItemQuantity(product, user, quantity));
    }, [dispatch, quantity, product, user]);

    return (
        <div className={styles.quantity}>
            <select
                value={quantity}
                onChange={(e) => {
                    setQuantity(e.target.value);
                }}>
                {[...Array(11).keys()].slice(1).map((num) => (
                    <option
                        key={num}
                        value={num}
                    >
                        {num}</option>))}
            </select>
            <div>
                {`$${(Math.round(quantity * product.price * 100) / 100).toFixed(2)}`}
            </div>
        </div>
    )
}
