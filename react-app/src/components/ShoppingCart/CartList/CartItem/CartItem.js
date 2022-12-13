export default function CartItem({ product_id, amount }) {
    return (
        <div>
            <div>{product_id}</div>
            <div>{amount}</div>
        </div>
    )
}
