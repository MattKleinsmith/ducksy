
export default function CartSummary() {
    const items = window.localStorage.getItem('products')
    const itemsNum = items ? items.length : 0
    return (
        <div>
            <div>
                {itemsNum} items in your cart
            </div>
        </div>
    )
};
