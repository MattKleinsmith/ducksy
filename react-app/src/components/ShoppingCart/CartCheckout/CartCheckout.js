import { useDispatch } from "react-redux"
import { checkoutCart } from "../../../store/shoppingCart"

export default function CartCheckout({ cart_items, user }) {
    const dispatch = useDispatch();

    return (
        <div className="CartCheckout">
            <button onClick={() => dispatch(checkoutCart(user))}
            >Proceed to checkout</button>
        </div>
    )
}
