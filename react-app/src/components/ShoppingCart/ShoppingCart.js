import { NavLink } from "react-router-dom";
import { useSelector, } from 'react-redux';
import CartSummary from "./CartSummary/CartSummary";
import styles from './ShoppingCart.module.css'
import { CartList } from "./CartList/CartList";
import CartCheckout from "./CartCheckout/CartCheckout";

export default function ShoppingCart() {
    const user = useSelector(state => state.session.user)
    const products = useSelector(state => state.products)
    const carts = useSelector(state => state.shoppingCarts)

    let current_cart = {}
    if (carts) current_cart = user ? carts[user.id] : carts["guest"]
    const cart_items = Object.entries(current_cart).filter(([product_id, quantity]) => product_id in products);

    return (
        <>
            {
                cart_items.length === 0 || !Object.keys(products).length ?
                    <div className={styles.wrapper}>
                        <h1>Your cart is empty</h1>
                        <NavLink to={'/'}>Discover something unique to fill it up</NavLink>
                    </div>
                    :
                    <div className={styles.wrapper}>
                        <CartSummary cart_items={cart_items} />
                        <div className={styles.grid}>
                            <CartList cart_items={cart_items} />
                            <CartCheckout cart_items={cart_items} user={user} />
                        </div>
                    </div>
            }
        </>
    )
}
