import { useNavigate } from "react-router";



export default function CartSummary() {
    const navigate = useNavigate();

    const totalItems = () => {
        let itemNum = 0;
        const cart = window.localStorage.getItem('ducksyCart');
        if (cart) {
            const items = JSON.parse(cart)
            itemNum = Object.values(items).reduce((total, num) => total += num, 0);
        }
        return itemNum;
    };

    return (
        <div className="cartSummary">
            <div>
                <h1>{totalItems()} items in your cart</h1>
            </div>
            <div>
                <button onClick={() => navigate('/')}>
                    Keep shopping</button>
            </div>
        </div>
    )
};
