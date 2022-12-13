import CartItem from "./CartItem/CartItem"


export function CartList({ cart }) {
    let cart_entries = cart ? Object.entries(cart) : null;

    console.log(cart_entries)
    return (
        <>
            {/* {cart_entries
                && cart_entries.map(([product_id, amount], i) => <CartItem product_id={Number(product_id)} amount={amount} key={i} />)}
            {!cart_entries
                && <div>
                    <h1>Your cart is empty</h1>
                </div>} */}
        </>
    )
}
