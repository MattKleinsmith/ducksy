import { useSelector } from "react-redux";
import { useNavigate } from "react-router";



export default function CartSummary({ carts }) {
    const navigate = useNavigate();
    const user = useSelector(state => state.session.user)
    console.log('CartSummary', carts)

    const totalItems = (carts) => {
        const current_cart = user ? carts[user.id] : carts["guest"]
        const itemNum = Object.values(current_cart).reduce((total, num) => total += num, 0);
        return itemNum;
    };

    return (
        <div className="cartSummary">
            <div>
                <h1>{totalItems(carts)} items in your cart</h1>
            </div>
            <div>
                <button onClick={() => navigate('/')}>
                    Keep shopping</button>
            </div>
        </div>
    )
};
