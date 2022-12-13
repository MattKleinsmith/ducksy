import { useNavigate } from "react-router";



export default function CartSummary({ cart }) {
    const navigate = useNavigate();

    const totalItems = (cart) => {
        let itemNum = 0;
        if (cart) {
            itemNum = Object.values(cart).reduce((total, num) => total += num, 0);
        }
        return itemNum;
    };

    return (
        <div className="cartSummary">
            <div>
                <h1>{totalItems(cart)} items in your cart</h1>
            </div>
            <div>
                <button onClick={() => navigate('/')}>
                    Keep shopping</button>
            </div>
        </div>
    )
};
