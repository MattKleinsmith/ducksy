import { useNavigate } from "react-router";
import "./ShopButton.css";

export default function ShopButton() {
    const navigate = useNavigate()
    return (
        <>
            <button className="shopButton" onClick={() => navigate("/your/shop")}>
                <i className="fa-solid fa-shop" />
            </button>
        </>
    );
}
