import styles from './CartCheckout.module.css'
import { useDispatch, useSelector } from "react-redux"
import { useNavigate } from "react-router";
import { checkoutCart } from "../../../store/shoppingCart"
import { setRegisterModal } from "../../../store/ui";


export default function CartCheckout({ cart_items, user }) {
    const dispatch = useDispatch();
    const navigate = useNavigate();
    const products = useSelector(state => state.products)
    const subtotal = cart_items.reduce((total, [product_id, quantity]) => total += products[product_id].price * quantity, 0)
    const checkoutHandler = user => {
        if (user) dispatch(checkoutCart(user))
            .then((orderId) => navigate(`/cart/checkout/${orderId}`))
        else dispatch(setRegisterModal(true))
    }
    return (
        <div className={styles.CartCheckout}>
            <div className={styles.cart_subtotal}>
                <div>
                    Item(s) total
                </div>
                <div>
                    {`$${(Math.round(subtotal * 100) / 100).toFixed(2)}`}
                </div>
            </div>
            <div className={styles.cart_checkout_button}>
                <button onClick={() => checkoutHandler(user)}
                >Proceed to checkout</button>
            </div>
        </div>
    )
}
