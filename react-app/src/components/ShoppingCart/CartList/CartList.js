import CartItem from "./CartItem/CartItem"


export function CartList({ cart }) {
    const cart_entries = Object.entries(cart)
    console.log(cart_entries)
    return (
        <>
            {cart_entries.map(([product_id, amount], i) => <CartItem product_id={Number(product_id)} amount={amount} key={i} />)}
        </>
    )
}
