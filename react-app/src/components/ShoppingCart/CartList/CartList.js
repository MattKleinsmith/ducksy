import { useSelector } from "react-redux"
import CartItem from "./CartItem/CartItem"
import './CartList.css'

export function CartList({ cart_items }) {
    const products = useSelector(state => state.products);

    return (
        <>
            {Object.keys(products).length > 0 &&
                <div className="CartList">
                    {cart_items.length > 0
                        && cart_items.map(([product_id, amount], i) => <CartItem product={products[product_id]} amount={amount} key={i} />)}
                </div>
            }
        </>
    )
}
