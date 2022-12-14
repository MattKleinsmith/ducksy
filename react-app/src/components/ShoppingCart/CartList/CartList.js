import { useSelector } from "react-redux"
import { NavLink } from "react-router-dom"
import CartItem from "./CartItem/CartItem"
import './CartList.css'

export function CartList({ carts }) {
    const user = useSelector(state => state.session.user)
    const products = useSelector(state => state.products)
    const current_cart = user ? carts[user.id] : carts["guest"]
    const cart_items = Object.entries(current_cart)

    return (
        <>
            {Object.keys(products).length > 0 &&
                <div className="CartList">
                    {cart_items.length > 0
                        && cart_items.map(([product_id, amount], i) => <CartItem product={products[product_id]} amount={amount} key={i} />)}
                    {cart_items.length === 0
                        && <div>
                            <h1>Your cart is empty</h1>
                            <NavLink to={'/'}>Discover something unique to fill it up</NavLink>
                        </div>}
                </div>
            }
        </>
    )
}
