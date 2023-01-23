import { NavLink, useNavigate } from "react-router-dom";
import { useDispatch, useSelector, } from 'react-redux';
import { useEffect, useState } from "react";
import styles from './ShoppingCart.module.css'
import CartSummary from "./CartSummary/CartSummary";
import CartCheckout from "./CartCheckout/CartCheckout";
import { CartList } from "./CartList/CartList";
import { getCarts } from "../../store/shoppingCart";
import { setDataLoadingModal } from "../../store/ui";

export default function ShoppingCart() {
    const navigate = useNavigate();
    const dispatch = useDispatch();
    const user = useSelector(state => state.session.user)
    const [isLoaded, setIsLoaded] = useState(false);
    const products = useSelector(state => state.products)
    const carts = useSelector(state => state.shoppingCarts)
    let current_cart = {}
    if (carts) current_cart = user ? carts[user.id] : carts["guest"]
    const cart_items = Object.entries(current_cart).filter(([product_id, quantity]) => product_id in products);

    useEffect(() => {
        if (!isLoaded) {
            dispatch(setDataLoadingModal(true));
            (async () => {
                await dispatch(getCarts(user));
                setIsLoaded(true)
                navigate("/cart");
            })();
        }
        else {
            dispatch(getCarts(user));
        }
    }, [dispatch, user]);

    if (!isLoaded) return null;

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
